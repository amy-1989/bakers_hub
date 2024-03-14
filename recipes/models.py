from django.db import models
from django.contrib.auth.models import User
from django.db.models import F
from cloudinary.models import CloudinaryField

STATUS = ((0, "Draft"), (1, "Published"))

RATING = (
    (1,"⭐☆☆☆☆"),
    (2,"⭐⭐☆☆☆"),
    (3,"⭐⭐⭐☆☆"),
    (4,"⭐⭐⭐⭐☆"),
    (5,"⭐⭐⭐⭐⭐")
    )


class Category(models.Model):
    title = models.CharField(max_length=200, unique=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return f"{self.title}"


class Post(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='', null=True, related_name='categorys')
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(max_length=200, unique=True, null=True)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="blog_posts"
    )
    featured_image = CloudinaryField('image', default='placeholder')
    ingredients = models.TextField(default='')
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    status = models.IntegerField(choices=STATUS, default=0)

    class Meta:
        ordering = ["-created_on"]

    def __str__(self):
        return f"{self.title} created by {self.author}"
    

class Comment(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="commenter")
    body = models.TextField()
    parent = models.ForeignKey(
        "self", null=True, blank=True, on_delete=models.CASCADE,
        related_name="replies")
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Comment: {self.body} by {self.author}"
    
  
class Review(models.Model):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="reviews")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="reviewer")
    approved = models.BooleanField(default=False)
    rating = models.IntegerField(choices=RATING, default=None) 

    def __str__(self):
        return f"{self.post}: {self.rating}"
