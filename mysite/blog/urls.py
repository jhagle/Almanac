from django.conf.urls import patterns, include, url
from django.views.generic import ListView, DetailView
from blog.models import Post


urlpatterns = patterns('',
    url(r'^$', ListView.as_view(
        queryset=Post.objects.all(),
        template_name="blog.html")),


    url(r'^(?P<pk>\d+)$', DetailView.as_view(
        model = Post,
        template_name="post.html")),

    url(r'^archives/$', ListView.as_view(
        queryset=Post.objects.all(),
        template_name="posttitleslist.html")),

    url(r'latestnews/$', ListView.as_view(
        queryset=Post.objects.all(),
        template_name="posttitleslist.html")),

)