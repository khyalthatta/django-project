from django.contrib import admin

from .models import Contact, Publisher, Article

admin.site.register(Contact)
admin.site.register(Publisher)
admin.site.register(Article)
