from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post,Author
from .forms import PostForm,EditForm
from django.urls import reverse_lazy

class HomeView(ListView):
    model = Post
    template_name = 'home.html'
    ordering = ['-date']
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Post
    template_name = 'blog_details.html'

class AddBlogView(CreateView):
    model = Post 
    form_class = PostForm
    template_name = 'add_blog.html'


class UpdateBlogView(UpdateView):
    model = Post
    template_name = 'update_blog.html'
    form_class = EditForm
    #fields = ['title' , 'body' , 'date']

class DeleteBlogView(DeleteView):
    model = Post
    template_name = 'delete_blog.html'
    success_url = reverse_lazy('home')

class AuthorView(ListView):
    model = Author
    template_name = 'authors.html'

class AuthorDetailView(ListView):
    model = Post
    template_name = 'author_details.html'

    


