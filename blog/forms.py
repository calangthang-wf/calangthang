from django import forms
from blog.models import newArticle, blogComment
from django.forms.widgets import ClearableFileInput

class CustomThumbnailWidget(ClearableFileInput):
    template_name = 'add_thumbnail.html'

class CustomImagesWidget(ClearableFileInput):
    template_name = 'upload_image.html'

class newArticleForm(forms.ModelForm):

    title = forms.CharField(
        required=True,
        max_length=100,
        widget=forms.TextInput(attrs={
            'class': 'post-input-title',
            'id': 'post-title',
            })
        )
    content = forms.CharField(
        required=True,
        max_length=3000, 
        widget=forms.Textarea(attrs={
            'id': 'editor',
            'style': 'width: 100%; height: 100%; border: none; outline: none;'
            })
        )
    
    thumbnail = forms.ImageField(
        required=True,
        widget=forms.FileInput(attrs={
            'id': 'thumbnail-input',
            'style': 'display: none;',
        })
    )

    class Meta:
        model = newArticle
        fields = ['title', 'content', 'thumbnail',]

class articleCommentForm(forms.ModelForm):

    body = forms.CharField(
        required=True,
        max_length=2000, 
        widget=forms.Textarea(attrs={
            'id': 'message',
            'rows': 6,
            'placeholder': 'Type your comment',
            }
        )
    )

    class Meta:
        model = blogComment
        fields = ['body']