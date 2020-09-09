from django.urls import path
from blog.views import (
    blog_view,
    detail_blog_view
    )

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name="blog_list"),
    path('<int:id>', detail_blog_view, name="blog_details"),
]
