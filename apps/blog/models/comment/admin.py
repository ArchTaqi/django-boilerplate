# -*- coding: utf-8 -*-
from django.contrib import admin
from .model import Comment

# Register your models here.


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    pass
