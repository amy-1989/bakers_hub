from django.contrib import admin
from .models import Post, Comment, Review, Category
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Post)
class PostAdmin(SummernoteModelAdmin):

    list_display = ('title', 'status', 'created_on')
    search_fields = ['title', 'content', ]
    list_filter = ('status', 'created_on',)
    prepopulated_fields = {'slug': ('title',)}
    summernote_fields = ('content', 'ingredients')


@admin.register(Review)
class ReviewAdmin(SummernoteModelAdmin):
    list_display = ('rating', 'approved', 'author',)
    search_fields = ['author', 'rating', ]
    list_filter = ('approved',)


@admin.register(Comment)
class CommentAdmin(SummernoteModelAdmin):
    list_display = ('body', 'approved', 'created_on',)
    search_fields = ['approved', 'created_on', ]
    list_filter = ('body', 'approved', 'created_on',)


admin.site.register(Category)
