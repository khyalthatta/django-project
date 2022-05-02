from django.db import models


class Blog(models.Model):
    title = models.CharField(max_length=50)
    content = models.TextField(blank=True, null=True)
    footer = models.CharField(max_length=50)

    def __str__(self):
        return self.title
