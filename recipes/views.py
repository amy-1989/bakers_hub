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
    comments = post.comments.filter(parent__isnull=True).order_by("created_on")
    comment_count = post.comments.filter(approved=True).count()
    reviews = post.reviews.all()

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


def post_delete(request, slug, post_id):
    """
    view to delete post
    """
    post = get_object_or_404(Post, slug=slug)
 
    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own recipes!')

    return HttpResponseRedirect('/')


def reply_edit(request, slug, reply_id):
    """
    view to edit replies
    """
    if request.method == "POST":
        reply = get_object_or_404(Comment, pk=reply_id)
        reply_form = ReplyForm(data=request.POST, instance=reply)

        if reply_form.is_valid() and reply.author == request.user:
            reply = comment_form.save(commit=False)
            reply.post = post
            reply.approved = False
            reply.save()
            messages.add_message(request, messages.SUCCESS, 'Reply Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating reply!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))


def reply_delete(request, slug, reply_id):
    """
    view to delete a reply
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    reply = get_object_or_404(Comment, pk=reply_id)

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


def post_edit(request, slug, post_id):

    current_post = Post.objects.get(id=post_id)

    if request.method == "POST":

        review = get_object_or_404(Post, pk=post_id)
        post_form = RecipePostForm(data=request.POST, instance=post)

        if post_form.is_valid() and post.author == request.user:
            post = rating_form.save(commit=False)
            post.post = post
            post.approved = False
            post.save()
            messages.add_message(request, messages.SUCCESS, 'Post Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating post!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))


def review_edit(request, slug, review_id):
    """
    view to edit reviews
    """
    if request.method == "POST":

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        review = get_object_or_404(Review, pk=review_id)
        rating_form = RatingForm(data=request.POST, instance=review)

        if rating_form.is_valid() and review.author == request.user:
            review = rating_form.save(commit=False)
            review.post = post
            review.approved = False
            review.save()
            messages.add_message(request, messages.SUCCESS, 'Review Updated!')
        else:
            messages.add_message(request, messages.ERROR, 'Error updating review!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))


def review_delete(request, slug, review_id):
    """
    view to delete reviews
    """
    queryset = Post.objects.filter(status=1)
    post = get_object_or_404(queryset, slug=slug)
    review = get_object_or_404(Review, pk=review_id)

    if review.author == request.user:
        review.delete()
        messages.add_message(request, messages.SUCCESS, 'Rating deleted!')
    else:
        messages.add_message(request, messages.ERROR, 'You can only delete your own ratings!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))
