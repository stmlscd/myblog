from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from .views import blog_list, blog_detail, post_like, search

urlpatterns = [
    path('', blog_list, name="list"),
    path('posts/<int:pk>/', blog_detail, name="detail"),
    path('like_posts/<int:pk>/', post_like, name="like"),
    path('post/search_results', search, name="search"),
    path('ckeditor/', include("ckeditor_uploader.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)