from django.contrib import admin
from blog.models import blogComment

class articleComment(admin.ModelAdmin):
    list_display = ['article', 'name', 'created_at']
    search_fields = ['name', 'created_at']
    list_filter = ['article', 'name']

admin.site.register(blogComment, articleComment)
