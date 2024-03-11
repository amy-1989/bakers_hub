from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment, Review
from .forms import CommentForm, RecipePostForm, RatingForm
from django.contrib import messages


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
    comments = post.comments.filter(approved=True, parent__isnull=True).order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()
    reviews = post.reviews.filter(approved=True)

    if request.method == "POST":

        rating_form = RatingForm(data=request.POST)

        if rating_form.is_valid():
            review = rating_form.save(commit=False)
            review.author = request.user
            review.post = post
            review.save()
            return HttpResponseRedirect(reverse('recipe_post', args=[slug]))
        else:
            rating_form = RatingForm()
            
        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            parent_obj = None
            try:
                parent_id = int(request.POST.get('parent_id'))
            except:
                parent_id = None
            if parent_id:
                parent_obj = Comment.objects.get(id=parent_id)
                if parent_obj:
                    reply_comment = comment_form.save(commit=False)
                    reply_comment.parent = parent_obj
            comment = comment_form.save(commit=False)
            comment.author = request.user
            comment.post = post
            comment.save()
            return HttpResponseRedirect(reverse('recipe_post', args=[slug]))
    else:
        comment_form = CommentForm()
        rating_form = RatingForm()

    return render(
                request,
                "recipes/post.html",
                {"post": post,
                "comments": comments,
                "reviews": reviews,
                "rating_form": rating_form,
                "comment_count": comment_count,
                "comment_form": comment_form,}
            )
        

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
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))


def reply_edit(request, slug, comment_id):
    """
    view to edit replies
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        reply = get_object_or_404(Comment, pk=comment_id)
        comment_form = CommentForm(data=request.POST, instance=comment)

        if comment_form.is_valid() and reply.author == request.user:
            reply = comment_form.save(commit=False)
            reply.post = post
            reply.approved = False
            reply.save()
            messages.add_message(request, messages.SUCCESS, 'Comment Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating comment!')

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
        messages.add_message(request, messages.SUCCESS, 'Comment deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own comments!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))

def post_delete(request, slug, comment_id):
    """
    view to delete comment
    """
    post = get_object_or_404(Post, slug=slug)
 
    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Post deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own posts!')

    return HttpResponseRedirect(reverse('/', args=[slug]))


def reply_delete(request, slug, comment_id):
    """
    view to delete a reply
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    reply = get_object_or_404(Comment, pk=comment_id)

    if reply.author == request.user:
        reply.delete()
        messages.add_message(request, messages.SUCCESS, 'Reply deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own replies!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))


def create_recipe_post(request):
    if request.method == "POST":
        recipe_post_form = RecipePostForm(data=request.POST)
        if recipe_post_form.is_valid():
            form = recipe_post_form.save(commit=False)
            form.author = request.user                  
            form.save()
            messages.add_message(request, messages.SUCCESS, "Recipe request sent! Awaiting admin approval!")
            return HttpResponseRedirect('recipe_post', args=[post_id])

    recipe_post_form = RecipePostForm()

    return render(
        request,
        "recipes/create_post.html",
        {"recipe_post_form":recipe_post_form},
    )


def edit_recipe_post():
    current_post = Post.objects.get(id=post_id)

    if post.author == request.user:
        if request.method != 'POST':
            
            form = RecipePostForm(instance=current_post)
        else:
            form = RecipePostFormForm(instance=current_post, data=request.POST)
            if form.is_valid():
                form.save()
                messages.add_message(request, messages.SUCCESS, 'Recipe Updated!')
            else:
                messages.add_message(request, messages.ERROR, 'Error updating recipe!')

                return HttpResponseRedirect(reverse('recipe_post', args=[slug]))

    context = {'post':post, 'form':form}
    return render(request, 'recipes/edit_post.html', context)



