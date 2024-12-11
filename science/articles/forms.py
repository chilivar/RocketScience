from django import forms
from .models import Article
from .models import Report

class ReportForm(forms.ModelForm):
    class Meta:
        model = Report
        fields = ['reason']
        widgets = {
            'reason': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Опишите причину жалобы...',
                'rows': 3,
            }),
        }
class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']  # Поля, которые будут отображаться в форме
        widgets = {
            'content': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Введите ваш комментарий...',
                'rows': 3
            }),
        }
