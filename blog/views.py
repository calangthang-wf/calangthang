from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from blog.models import newArticle, blogComment
from blog.forms import newArticleForm, articleCommentForm

def blog_home(request):
    urArticle = newArticle.objects.all()
    return render(request, 'blog.html', {'post': urArticle})

def detail(request, slug):

    article = get_object_or_404(newArticle, slug=slug)

    if request.method == "POST":
        cmt = articleCommentForm(request.POST)    

        if cmt.is_valid():
            comment = cmt.save(commit=False)
            comment.article = article
            comment.name = request.user
            comment.save()
            return redirect('detail', slug=slug)        
    else:
        cmt = articleCommentForm()   

    return render(request, 'detail.html', {'detail': article, 'cmt': cmt})

"""
def detailComments(request, slug):
    comments = get_object_or_404(blogComment, slug=slug)
    return render(request, 'detail.html', {'cmts', comments})
"""

def blog_upload(request):

    form = newArticleForm(request.POST)

    if request.method == "POST":
        form = newArticleForm(request.POST, request.FILES)
        if form.is_valid():
            thumbnail = form.cleaned_data['thumbnail']

            new_article = form.save(commit=False)

            new_article.author = request.user

            new_article.save()

            new_article.thumbnail = thumbnail
            new_article.save()

            return redirect('/blog')
        else:
            print(form.errors)

    else:
        form = newArticleForm()
        print("Request.GET")

    return render(request, 'blog_upload.html', {"form": form})