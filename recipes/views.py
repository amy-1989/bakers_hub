from django.shortcuts import render,  get_object_or_404, reverse
from django.views import generic
from django.http import HttpResponseRedirect
from .models import Post, Category, Comment, Review
from .forms import CommentForm, RecipePostForm, RatingForm, ReplyForm
from django.contrib import messages


class CategoryList(generic.ListView):
    queryset = Category.objects.all()
    template_name = "recipes/index.html"
    paginate_by = 6


def recipe_category(request, category):
    posts = Post.objects.filter(
        category__title__icontains=category, status=1
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
            except TypeError:
                parent_id = None
                print('There is no parent id! This will be a new comment!')
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
                 "comment_form": comment_form, }
            )


def edit_post(request, post_id=None):

    posts = Post.objects.all()

    if post_id:
        post = get_object_or_404(Post, pk=post_id)
        post_form = RecipePostForm(instance=post)
    else:
        post_form = RecipePostForm()

    if request.method == 'POST':
        if post_id:
            post = get_object_or_404(Post, pk=post_id)
            post_form = RecipePostForm(request.POST,
                                       request.FILES, instance=post)
        else:
            post_form = RecipePostForm(request.POST, request.FILES)
        if post_form.is_valid():
            post_form.save()
            messages.success(request, "Recipe edited successfully!")
        return HttpResponseRedirect('/')

    return render(request, 'recipes/edit_post.html', {
        'post': post if post_id else None,
        'post_form': post_form,
        'posts': posts
        })


def post_delete(request, slug, post_id):
    """
    view to delete post
    """
    post = get_object_or_404(Post, slug=slug)

    if post.author == request.user:
        post.delete()
        messages.add_message(request, messages.SUCCESS, 'Recipe deleted!')
    else:
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own recipes!')

    return HttpResponseRedirect('/')


def create_recipe_post(request):
    posts = Post.objects.all()

    if request.method == 'POST':
        recipe_post_form = RecipePostForm(request.POST, request.FILES)
        if recipe_post_form.is_valid():
            recipe_post = recipe_post_form.save(commit=False)
            recipe_post.featured_image = request.FILES['featured_image']
            recipe_post.author = request.user
            recipe_post.save()
            messages.success(request,
                             "Recipe request sent! Awaiting admin approval!")
            return HttpResponseRedirect('/')
    else:
        recipe_post_form = RecipePostForm()

    return render(request, 'recipes/create_post.html', {
        'posts': posts,
        'recipe_post_form': recipe_post_form
    })


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
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own comments!')

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
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own replies!')

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
            messages.add_message(request, messages.ERROR,
                                 'Error updating review!')

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
        messages.add_message(request, messages.ERROR,
                             'You can only delete your own ratings!')

    return HttpResponseRedirect(reverse('recipe_post', args=[slug]))
