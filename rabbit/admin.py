# -*- coding: utf-8 -*-


# django related
from django.contrib import admin

# local modules
from .models import Comment, Post, SubRabbit


@admin.register(SubRabbit)
class SubRabbitAdmin(admin.ModelAdmin):
    """
    'name',
    'title',
    'description',
    'sidebar',
    'submission_text',
    'datetime_created',
    'suspended',
    'banned',
    'deleted',
    'owner',
    'moderators',
    'members',
    """

    list_display = [
        'name',
        'suspended',
        'banned',
        'deleted',
        'owner',
    ]

    fields = [
        ('name', 'title'),
        'owner',
        'description',
        'sidebar',
        'submission_text',
        'datetime_created',
        ('suspended', 'banned', 'deleted'),
        'moderators',
        'members',
    ]

    list_filter = [
        'name',
        'suspended',
        'banned',
        'deleted',
        'owner',
    ]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    """
    'post_type',
    'title',
    'content',
    'deleted',
    'datetime_submitted',
    'datetime_last_edited',
    'points',
    'subrabbit',
    'poster',
    'score',
    """

    list_display = [
        'post_type',
        'title',
        'deleted',
        'subrabbit',
        'poster',
        'points',
        'datetime_submitted',
    ]

    fields = [
        'subrabbit',
        'poster',
        'title',
        'post_type',
        'content',
        'deleted',
        'datetime_last_edited',
        'points',
    ]

    list_filter = [
        'post_type',
        'title',
        'deleted',
        'subrabbit',
        'poster',
        'datetime_submitted',
        'points',
    ]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    """
    'contents',
    'score',
    'datetime_submitted',
    'datetime_last_edited',
    'deleted',
    'top_level',
    'author',
    'subrabbit',
    'post',
    'parent',
    """

    list_display = [
        'points',
        'datetime_submitted',
        'deleted',
        'author',
        'subrabbit',
        'post',
    ]

    fields = [
        'subrabbit',
        'author',
        'points',
        ('datetime_submitted', 'datetime_last_edited'),
        'deleted',
        'top_level',
        'post',
        'parent',
        'contents',
    ]

    list_filter = [
        'deleted',
        'author',
        'subrabbit',
        'post',
    ]
