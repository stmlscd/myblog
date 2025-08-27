from django.urls import path
from .views import blog_list, blog_detail, post_like, search

urlpatterns = [
    path('', blog_list, name="list"),
    path('posts/<int:pk>/', blog_detail, name="detail"),
    path('like_posts/<int:pk>/', post_like, name="like"),
    path('post/search_results', search, name="search")
]