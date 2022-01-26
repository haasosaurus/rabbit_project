# -*- coding: utf-8 -*-


# django related
from django.contrib.auth import views as auth_views
from django.urls import path, re_path

# local modules
from . import views


urlpatterns = [
    path(route='', view=views.index, name='index'),
    # path(route='', view=auth_views.LoginView.as_view(template_name='rabbit/login.html'), name='index'),
    path(route='register/', view=views.RegisterView.as_view(), name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='rabbit/login.html'), name='login'),
    path('logout/', view=auth_views.LogoutView.as_view(), name='logout'),
    path('profile/', view=views.ProfileView.as_view(), name='profile'),
    path('r/<str:pk>/', view=views.subrabbit_view, name='sub')
    # path('r/<str:pk>/', view=views.SubRabbitPostsListsView.as_view(), name='sub')


    # re_path(r'^(?i)r/(?P<name>[a-zA-Z_]+)$', views.subrabbit_view, name='sub')
    # re_path(r'^(?i)r/(?P<str>[a-zA-Z_]+)$', views.subrabbit_view, name='sub')
    # path('logout/', view=auth_views.LogoutView.as_view(template_name='rabbit/logout.html'), name='logout'),
]





"""
https://stackoverflow.com/questions/12918464/in-django-how-do-you-write-the-url-pattern-for-and-other-root-based-urls/12918862
"""

'''
project urls
'''

#  urlpatterns = patterns('',
#     url(r'^polls/', include('polls.urls')),
#     url(r'^$', 'pages.views.root'),
#     url(r'', include('pages.urls')),
#  )

'''
app urls
'''

#  from django.conf.urls import patterns, include, url
#  urlpatterns = patterns('pages.views',
#       url(r'^about', 'about'),
#  )
