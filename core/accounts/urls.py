from django.urls import path
from . import views

urlpatterns = [
    path('facebook/login', views.FacebookLoginView.as_view(), name='facebook_login'),
    path('google/login', views.GoogleLoginView.as_view(), name='google_login')
]
