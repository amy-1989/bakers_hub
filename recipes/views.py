from django.shortcuts import render
from django.views import generic
from .models import Post
from .models import Category

# Create your views here.

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "recipes/index.html"
    paginate_by = 6

class PostList(generic.ListView):
    queryset = Post.objects.filter(status = 1)
    template_name = "recipes/index.html"
    paginate_by = 6
