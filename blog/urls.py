from django.urls import path
from blog import views

urlpatterns = [
    path('', views.blog_home, name='blog_home'),
    path('articleupload', views.blog_upload, name="article_upload"),
    path('<slug:slug>', views.detail, name="detail"),
]