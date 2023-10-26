from django.shortcuts import render
from django.http import HttpResponse

from home.models import blogPosts, communityList, popularPost, popularService
# Create your views here.

def home(request):

    blog_list = blogPosts.objects.all
    comunity_list = communityList.objects.all
    popular_posts_list = popularPost.objects.all
    popular_service_list = popularService.objects.all

    return render(request, 'home.html', {
        'all_blog_list': blog_list, 
        'all_comunity_list': comunity_list,
        'all_popular_posts_list': popular_posts_list,
        'popular_service_lists': popular_service_list,
        })