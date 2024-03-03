from .models import Comment
from django import forms


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

class ReplyForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('body',)

#class RecipePostForm(forms.ModelForm):
 #   class Meta:
  #      model = Post
   #     fields = ('title', 'featured image', 'ingredients', 'content',)
