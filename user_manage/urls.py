from django.urls import path
from user_manage import views

urlpatterns = [
    path('', views.userIndex, name='user'),
    path('register', views.register, name="register"),
    path('login', views.user_login, name="login"),
    path('logout', views.user_logout, name="logout"),
]
