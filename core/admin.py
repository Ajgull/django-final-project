from django.contrib import admin

from core import models


@admin.register(models.Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = (
        'user',
        'bio'
    )


@admin.register(models.Post)
class PostAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'text',
        'image'
    )


@admin.register(models.Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'text',
        'post'
    )


@admin.register(models.Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = (
        'author',
        'post'
    )
