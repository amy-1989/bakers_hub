from .models import Comment, Post
from django import forms
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipePostForm(forms.ModelForm):

    featured_image = CloudinaryFileField()

    class Meta:
        model = Post
        fields = ('title', 'category', 'featured_image', 'ingredients', 'content',)
