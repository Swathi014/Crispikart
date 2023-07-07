from django.urls import path
from . import views

urlpatterns = [
    # path('', views.login),
    path('login', views.sign_in, name='sign-in'),
    path('logout',views.signout, name='sign-out')
]
