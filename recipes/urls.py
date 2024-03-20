from . import views
from django.urls import path



urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('create-post/', views.create_recipe_post, name='create_post'),
    path('edit-post/<int:post_id>', views.edit_post, name='edit_post'),
    path("category/<category>/", views.recipe_category, name="recipe_category"),
    path('<slug:slug>/', views.recipe_post, name='recipe_post'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),   
    path('<slug:slug>/delete_post/<int:post_id>',
         views.post_delete, name='post_delete'),
    path('<slug:slug>/delete_reply/<int:reply_id>',
         views.reply_delete, name='reply_delete'),
    path('<slug:slug>/edit_review/<int:review_id>',
         views.review_edit, name='review_edit'),
    path('<slug:slug>/delete_review/<int:review_id>',
         views.review_delete, name='review_delete'),

     
     
]
