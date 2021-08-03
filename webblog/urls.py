from django.urls import path, include
from .views import HomeView, BlogDetailView, AddBlogView, UpdateBlogView, DeleteBlogView, AuthorView, AuthorDetailView

urlpatterns = [
    path('', HomeView.as_view(), name="home"),
    path('blog/<int:pk>', BlogDetailView.as_view(), name='blog-detail'),
    path('add_blog/', AddBlogView.as_view(), name='add-blog'),
    path('blog/edit/<int:pk>', UpdateBlogView.as_view(), name='update-blog'),
    path('blog/<int:pk>/remove', DeleteBlogView.as_view(), name='delete-blog'),
    path('authors', AuthorView.as_view(), name="author"),
    path('authors/author/<int:pk>', AuthorDetailView.as_view(), name='author-detail'),

]