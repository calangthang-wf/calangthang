from django.contrib import admin
from home.models import blogPosts, communityList, popularPost, popularService
from blog.models import newArticle

class newArticleAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title', 'author']
    list_filter = ['author']
    prepopulated_fields = {"slug": ("title",)}

class ArticleInfomaion(admin.ModelAdmin):
    list_display = ['title', 'author']
    search_fields = ['title', 'author']
    list_filter = ['author']

class communityAdmin(admin.ModelAdmin):
    list_display = ['title']
    search_fields = ['title']
    list_filter = ['title']

admin.site.register(blogPosts, ArticleInfomaion)
admin.site.register(communityList, communityAdmin)
admin.site.register(popularPost, ArticleInfomaion)
admin.site.register(popularService, communityAdmin)
admin.site.register(newArticle, newArticleAdmin)
