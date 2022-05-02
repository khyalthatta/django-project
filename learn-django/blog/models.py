from django.db import models


class Contact(models.Model):
    fullname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    contact = models.CharField(max_length=10)
    message = models.TextField(max_length=1000)

    def __str__(self):
        return self.fullname


class Publisher(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=30)

    def __str__(self):
        return self.name


class Article(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=1000)
    publisher = models.ForeignKey(
        Publisher, on_delete=models.CASCADE, related_name='publisher_articles')

    def __str__(self):
        return self.title
