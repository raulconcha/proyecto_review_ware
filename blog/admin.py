from django.contrib import admin
from django.contrib.auth.models import Permission
from .models import Post, News

admin.site.register(Post)
admin.site.register(News)
admin.site.register(Permission)


