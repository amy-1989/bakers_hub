from .models import Comment, Post, Review
from django import forms
from cloudinary.forms import CloudinaryFileField


class CommentForm(forms.ModelForm):
    body = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = Comment
        fields = ('body',)

class ReplyForm(forms.ModelForm):
    body = forms.CharField(label ="", widget = forms.Textarea(
    attrs ={
        'class':'form-control',
        'placeholder':'Comment here !',
        'rows':4,
        'cols':50
    }))
    class Meta:
        model = Comment
        fields = ('body',)

class RecipePostForm(forms.ModelForm):

    featured_image = CloudinaryFileField()

    class Meta:
        model = Post
        fields = ('title', 'category', 'featured_image', 'ingredients', 'content',)

class RatingForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('rating',)

class CreatePostForm(forms.ModelForm):

    featured_image = CloudinaryFileField()

    class Meta:
        model = Post
        fields = ('title', 'category', 'featured_image', 'ingredients', 'content',)
