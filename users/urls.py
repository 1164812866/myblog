from django.urls import path
from . import views
 
app_name = 'users'

urlpatterns = [
    path('profile/', views.profile, name='profile'),
    path('profile/change/', views.change_profile, name='change_profile'),
]