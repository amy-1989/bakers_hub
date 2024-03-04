from .models import Comment, Post
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class RecipePostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'featured_image', 'ingredients', 'content',)
