from . import views
from django.urls import path

urlpatterns = [
    path('', views.about_bakershub, name='about'),
]
