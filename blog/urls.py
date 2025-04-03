from django.urls import path
from .views import blog_view, blog_details_view

app_name = 'blog'

urlpatterns = [
    path('', blog_view, name='blog'),
    path('blog-details/', blog_details_view, name='blog-details'),
]
