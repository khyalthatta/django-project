from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.viewsets import ModelViewSet
from rest_framework.permissions import AllowAny, IsAuthenticated
# from rest_framework.pagination import LimitOffsetPagination
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend

from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    UpdateAPIView,
    RetrieveAPIView,
    DestroyAPIView
)

from blog.models import Contact, Article
from .serializers import ContactSerializer, ArticleSerializer
from blog.permissions import IsSuperUser, project_permission


class SimpleAPIView(APIView):
    def get(self, *args, **kwargs):
        return Response({'message': 'DRF Created Successfully!'})


class ContactView(APIView):
    permission_classes = [AllowAny]

    def get(self, *args, **kwargs):
        contact_instance = Contact.objects.all()
        serializer = ContactSerializer(contact_instance, many=True).data
        return Response(serializer)

    def post(self, *args, **kwargs):
        deserializer = ContactSerializer(data=self.request.data)

        if deserializer.is_valid(raise_exception=True):
            deserializer.save()
            return Response({'message': 'Data Created'}, status=status.HTTP_201_CREATED)


class ContactListView(ListAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactCreateView(CreateAPIView):
    serializer_class = ContactSerializer


class ContactUpdateView(UpdateAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactRetrieveView(RetrieveAPIView):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactDestroyView(DestroyAPIView):
    serialzier_class = ContactSerializer
    queryset = Contact.objects.all()


class ContactModelViewSet(ModelViewSet):
    serializer_class = ContactSerializer
    queryset = Contact.objects.all()
    # pagination_class = LimitOffsetPagination
    # To override the methods of ModelViewSet

    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ['fullname', 'email', 'contact', 'message']
    filter_fields = ['contact', 'email']

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context['New Context'] = 'This context is added by user'
        return context

    def get_permissions(self):
        if self.action in ['list', 'retreive', ]:
            return [IsAuthenticated()]

        elif self.action == 'create':
            return [project_permission(['CCC'])()]

        return []


class ArticleModelViewSet(ModelViewSet):
    serializer_class = ArticleSerializer
    queryset = Article.objects.all()
