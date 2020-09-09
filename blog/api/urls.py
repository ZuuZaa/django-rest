from django.urls import path
from blog.api.views import api_blog_view, api_detail_blog_view

app_name = 'blog'

urlpatterns = [
    path('', api_blog_view, name='blog'),
    path('<int:id>', api_detail_blog_view, name="blog_details"),
]

