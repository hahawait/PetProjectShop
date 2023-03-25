from django.urls import path
from django.contrib.auth import views
from .views import register, profile

app_name = 'user'

urlpatterns = [
    path('register/', register, name='register'),
    path('profile/', profile, name='profile'),
    path('login/', views.LoginView.as_view(template_name='user/login.html'), name='login'),
    path('logout/', views.LogoutView.as_view(template_name='user/logout.html'), name='logout'),
]
