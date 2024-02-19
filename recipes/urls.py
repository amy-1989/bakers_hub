from . import views
from django.urls import path

urlpatterns = [
    path('', views.CategoryList.as_view(), name='home'),
    path("category/<category>/", views.recipe_category, name="recipe_category"),
]
