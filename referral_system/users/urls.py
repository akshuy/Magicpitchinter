from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_user, name='register'),
    path('details/', views.user_details, name='details'),
    path('referrals/', views.user_referrals, name='referrals'),
]
