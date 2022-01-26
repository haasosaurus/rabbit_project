# -*- coding: utf-8 -*-


# standard library modules
from datetime import datetime, timedelta

# django related
from django.db import models
from django.forms import ValidationError
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


def validate_subrabbit_name_case_insensitive(name):
    if SubRabbit.objects.filter(name_lower__iexact=name).exists():
        raise ValidationError(f"Subrabbit '{name}' already exists.")
    return name


class SubRabbit(models.Model):
    """
    model representing a subrabbit
    """

    name_lower = models.CharField(
        max_length=50,
        unique=True,
        validators=[
            validate_subrabbit_name_case_insensitive,
            RegexValidator(
                regex='^[a-zA-Z0-9][a-zA-Z0-9_]*$',
                message='Invalid Subrabbit name',
                code='invalid_subrabbit_name',
            ),
        ],
        default=None,
        null=True,
    )
    name = models.CharField(max_length=50, primary_key=True, null=False, unique=True)

    title = models.CharField(max_length=200, verbose_name='Title')
    description = models.TextField(max_length=500, verbose_name='Description')
    sidebar = models.TextField(max_length=10_240, verbose_name='Sidebar')
    submission_text = models.TextField(max_length=1_024, verbose_name='Submission text')

    datetime_created = models.DateTimeField(verbose_name='Date created', null=False)
    suspended = models.BooleanField(default=False, verbose_name='Currently suspended')
    banned = models.BooleanField(default=False, verbose_name='Currently banned')
    deleted = models.BooleanField(default=False, verbose_name='Deleted')

    owner = models.ForeignKey(User, null=True, verbose_name='Owner', on_delete=models.SET_NULL)

    moderators = models.ManyToManyField(User, verbose_name='Moderators', related_name='mod_of_subs')
    members = models.ManyToManyField(User, verbose_name='Members', related_name='member_of_subs')

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.name_lower = self.name.lower()
        super(SubRabbit, self).save(*args, **kwargs)


class Post(models.Model):
    """
    model representing a post
    """

    LINK = 'LINK'
    TEXT = 'TEXT'
    POST_TYPES = (
        (LINK, 'Link'),
        (TEXT, 'Text'),
    )
    post_type = models.CharField(
        max_length=4,
        choices=POST_TYPES,
        default=LINK,
        verbose_name='Post Type',
        help_text='Post type',
    )

    title = models.CharField(max_length=300, verbose_name='Post Title')
    content = models.TextField(max_length=40_000, verbose_name='Content')

    deleted = models.BooleanField(default=False, verbose_name='Deleted')
    datetime_submitted = models.DateTimeField(verbose_name='Date submitted', auto_now_add=True)
    datetime_last_edited = models.DateTimeField(verbose_name='Date last edited', null=True, blank=True)
    points = models.IntegerField(verbose_name='Points', default=0)

    subrabbit = models.ForeignKey(SubRabbit, verbose_name='Posted in', null=True, on_delete=models.SET_NULL)
    poster = models.ForeignKey(User, verbose_name='Poster', null=True, on_delete=models.SET_NULL)

    @property
    def score(self):
        # need to make time_penalty static once it stops changing

        delta: timedelta = datetime.now() - self.datetime_submitted
        hours = delta.total_seconds() // 3600
        if hours > 23:
            time_penalty = 9
        else:
            time_penalty = max(0, hours - 14)
        time_penalty /= 10
        return self.points * time_penalty

    def __str__(self):
        return f'{self.pk} {self.title[:60]}'


class Comment(models.Model):
    """
    model representing a comment on a post
    """

    contents = models.TextField(max_length=10_000)
    points = models.IntegerField(verbose_name='Points', default=0)
    datetime_submitted = models.DateTimeField(verbose_name='Date submitted')
    datetime_last_edited = models.DateTimeField(verbose_name='Date last edited', null=True, blank=True)
    deleted = models.BooleanField(default=False)
    top_level = models.BooleanField(default=False)

    author = models.ForeignKey(to=User, verbose_name='Author', null=True, on_delete=models.SET_NULL)
    subrabbit = models.ForeignKey(SubRabbit, verbose_name='Subrabbit', null=True, on_delete=models.SET_NULL)
    post = models.ForeignKey(Post, verbose_name='Post', null=True, on_delete=models.SET_NULL)
    parent = models.ForeignKey('Comment', verbose_name='Parent', null=True, on_delete=models.SET_NULL, blank=True)

    def __str__(self):
        return f'{self.author} - {self.post} - {self.datetime_submitted}'


# class Members(models.Model):
#     """
#     model representing a subrabbit member
#     """

#     member = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     sub = models.ForeignKey(SubRabbit, on_delete=models.CASCADE, null=False)


# class Moderators(models.Model):
#     """
#     model representing a subrabbit moderator
#     """

#     mod = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
#     sub = models.ForeignKey(SubRabbit, on_delete=models.CASCADE, null=False)
