from . import views
from django.urls import path



urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path('create-post/', views.create_recipe_post, name='create_post'),
    path('edit_post/<int:post_id>/', views.edit_recipe_post, name='edit_recipe'),
    path("category/<category>/", views.recipe_category, name="recipe_category"),
    path('<slug:slug>/', views.recipe_post, name='recipe_post'),
    path('<slug:slug>/edit_comment/<int:comment_id>',
         views.comment_edit, name='comment_edit'),
    path('<slug:slug>/delete_comment/<int:comment_id>',
         views.comment_delete, name='comment_delete'),
     path('<slug:slug>/delete_post/<int:post_id>',
         views.post_delete, name='post_delete'),
     
     
]
