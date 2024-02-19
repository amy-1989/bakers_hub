from django.shortcuts import render,  get_list_or_404
from django.views import generic
from .models import Post
from .models import Category

# Create your views here.

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "recipes/index.html"
    paginate_by = 6

def recipe_category(request, category):
    posts = Post.objects.filter(
        category__title__contains =category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "recipes/category.html", context)

