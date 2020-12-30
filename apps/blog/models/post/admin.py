# -*- coding: utf-8 -*-
from django.contrib import admin
from .model import Post

# Register your models here.


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass
