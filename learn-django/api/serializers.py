from rest_framework import serializers

from blog.models import (
    Contact,
    Publisher,
    Article
)


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'

    def create(self, validated_data):
        return super().create(validated_data)

    def validate_email(self, email):
        if 'gmail' in email:
            raise serializers.ValidationError(
                "Email Not Registered Yet. Please sign up to gmail account. ")
        return email


class PublisherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Publisher
        fields = '__all__'


class ArticleSerializer(serializers.ModelSerializer):

    # publisher = PublisherSerializer()
    total_publishers = serializers.SerializerMethodField()

    class Meta:
        model = Article
        fields = ['title', 'content', 'publisher', 'total_publishers']

    def get_fields(self):
        fields = super().get_fields()
        request = self.context.get('request')
        if request and request.method == 'GET':
            fields['publisher'] = PublisherSerializer()
        return fields

    def get_total_publishers(self, obj):
        return Publisher.objects.all().count()
