from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='profiles'),
    path('add', views.addProfile, name="addProfile")
]