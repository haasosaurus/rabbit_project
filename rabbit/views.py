# -*- coding: utf-8 -*-


# django related
from datetime import datetime
from django.contrib.auth.forms import UserCreationForm
from django.core.paginator import Paginator
from django.http import HttpRequest, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.views import generic, View
from django.urls import reverse

# local modules
from .models import Comment, Post, SubRabbit
from .forms import CreatePostForm
from .utils import image_scraper


def index(request: HttpRequest):
    """
    home page view function
    """

    post_list = Post.objects.all().order_by('-datetime_submitted')
    paginator = Paginator(post_list, 15)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'is_paginated': True,
    }
    return render(request, template_name='index.html', context=context)

class ProfileView(View):
    def get(self, request: HttpRequest):
        context = {}
        return render(request, template_name='rabbit/profile.html', context=context)


class RegisterView(View):
    def get(self, request: HttpRequest):
        return render(request, template_name='rabbit/register.html', context={'form': UserCreationForm()})

    def post(self, request: HttpRequest):
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            return redirect(reverse('login'))

        return render(request, template_name='rabbit/register.html', context={'form': form})


def subrabbit_view(request: HttpRequest, pk):
    sub = SubRabbit.objects.get(pk=pk)
    # post_list = Post.objects.filter(subrabbit__pk=pk).order_by('points')
    post_list = Post.objects.filter(subrabbit__pk=pk).order_by('-datetime_submitted')
    paginator = Paginator(post_list, 18)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {
        'page_obj': page_obj,
        'is_paginated': True,
        'sub': sub,

        # 'sub_name': sub.name,
        # 'sub_title': sub.title,
        # 'sub_description': sub.description,
        # 'sub_sidebar': sub.sidebar,
        # 'sub_submission_text': sub.submission_text,
        # 'sub_datetime_created': sub.datetime_created,
        # 'sub_owner': sub.owner,
        # 'sub_member_count': sub.members.all().count(),
        # 'sub_suspended': sub.suspended,
        # 'sub_banned': sub.banned,
        # 'sub_deleted': sub.deleted,
        # 'sub_moderators': sub.moderators,
    }

    return render(request, 'rabbit/subrabbit.html', context=context)





def post_detail_view(request: HttpRequest, sub_pk, post_pk):
    sub = SubRabbit.objects.get(pk=sub_pk)
    post = Post.objects.get(pk=post_pk)
    context = {
        'post': post,
        'sub': sub,
    }
    return render(request, 'rabbit/post_detail.html', context=context)




# class PostDetailView(generic.DetailView):
#     template_name = 'rabbit/post_detail.html'
#     model = Post



def create_post_view(request: HttpRequest, pk):
    sub = SubRabbit.objects.get(pk=pk)
    if request.method == 'POST':
        form = CreatePostForm(request.POST)
        if form.is_valid:
            post: Post = form.save(commit=False)
            post.datetime_submitted = datetime.now()
            post.subrabbit = sub
            post.poster = request.user
            post.points = 1

            if post.post_type == post.LINK:
                post_image = image_scraper(post.content)
                if post_image:
                    post.image_url = post_image

            post.save()
            return HttpResponseRedirect(reverse('post-detail', kwargs={'sub_pk': pk, 'post_pk': post.pk}))

    else:
        form = CreatePostForm()
        context = {
            'form': form,
            'sub': sub,
        }

    return render(request, 'rabbit/create_post.html', context=context)
