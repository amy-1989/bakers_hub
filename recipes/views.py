from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment
from .forms import CommentForm

# Create your views here.

class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "recipes/index.html"
    paginate_by = 6

def recipe_category(request, category):
    posts = Post.objects.filter(
        category__title__icontains = category
    ).order_by("-created_on")
    context = {
        "category": category,
        "posts": posts,
    }
    return render(request, "recipes/category.html", context)


def recipe_post(request, slug):
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comments = post.comments.all().order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()
    if request.method == "POST":
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            parent_obj=None
        try:
            parent_id = int(request.POST.get("parent_id"))
        except:
            parent_id=None

        if parent_id:
            parent_obj = Comment.objects.get(id=parent_id)
            if parent_obj:
                reply_comment = comment_form.save(commit=False)
                reply_comment.parent = parent_obj

        comment = comment_form.save(commit=False)
        comment.author = request.user
        comment.post = post
        comment.parent = parent_obj
        comment.save()

    comment_form = CommentForm()

    return render(
        request,
        "recipes/post.html",
        {"post": post,
        "comments": comments,
        "comment_count": comment_count,
        "comment_form": comment_form,},
    )

def comment_reply(request, slug, parent_id):
    if request.method == "POST":
       # replies=post.comments.filter()####check this filter
        reply_form = CommentForm(data=request.POST)

        if reply_form.is_valid():
            post_id = request.POST.get('post_id')
            parent_id = request.POST.get('parent_id')
            post_url = request.POST.get('post_url')

            reply = reply_form.save(commit=False)

            reply.post = Post(id=post_id)
            reply.parent = Comment(id=parent_id)
            reply.save()
        
        reply_form=CommentForm()
            

    return  HttpResponseRedirect(reverse('recipe_post', args=[slug]))


    
def comment_edit(request, slug, comment_id):
    """
    view to edit comments
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comment = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and comment.author == request.user:
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.approved = False
            comment.save()
#            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
 #       else:
  #          messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))

    
def comment_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    comment = get_object_or_404(Comment, pk=comment_id)

    if comment.author == request.user:
        comment.delete()
#        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
 #   else:
  #      messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))
