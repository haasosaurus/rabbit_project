# -*- coding: utf-8 -*-


# standard library
import datetime

# django related
from django import forms
from django.core.exceptions import ValidationError
from django.core.validators import URLValidator
from django.utils.translation import gettext_lazy as _


# local
from rabbit.models import Post


class CreatePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'content', 'post_type')
        labels = {
            'title': 'Title',
            'content': 'URL/Text',
            'post_type': 'Post Type',
        }
        help_texts = {
            'title': 'Enter your post title here',
            'content': 'Use a URL for a URL-type post, or enter the content of your text post',
            'post_type': 'Choose your post type'
        }
        error_messages = {
            'content': {
                'invalid_url': _('Invalid URL'),
            },
        }

    def clean(self):
        post_type = self.cleaned_data.get('post_type')
        if post_type != Post.TEXT:
            url = self.cleaned_data.get('content')
            validator = URLValidator()
            try:
                validator(url)
            except ValidationError:
                self.add_error(field='content', error='invalid_url')

        return self.cleaned_data
