from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.http import HttpResponseForbidden
from django.shortcuts import render, get_object_or_404, redirect
from .models import Article, Comment, Like
from .forms import ArticleForm, CommentForm, ReportForm
from django.urls import reverse

def article_list(request):
    query = request.GET.get('q')  # Получаем значение из строки запроса
    if query:
        articles = Article.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(author__username__icontains=query)  # Поиск по имени автора
        ).order_by('-created_at')
    else:
        articles = Article.objects.all().order_by('-created_at')  # Если запрос пуст, показываем все статьи

    return render(request, 'articles/all_articles.html', {'articles': articles, 'query': query})
def article_detail(request, pk):
    article = get_object_or_404(Article, pk=pk)
    comments = article.comments.all()
    form = CommentForm()
    report_form = ReportForm()  # Форма для жалобы

    is_liked = False
    if request.user.is_authenticated:
        is_liked = article.likes.filter(user=request.user).exists()

    if request.method == 'POST':
        if 'comment_submit' in request.POST:
            # Обработка комментариев
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.article = article
                comment.author = request.user
                comment.save()
                return redirect('articles:article_detail', pk=article.pk)
        elif 'report_submit' in request.POST:
            # Обработка жалоб
            report_form = ReportForm(request.POST)
            if report_form.is_valid():
                report = report_form.save(commit=False)
                report.article = article
                report.user = request.user
                report.save()
                return redirect('articles:article_detail', pk=article.pk)

    return render(request, 'articles/article_detail.html', {
        'article': article,
        'comments': comments,
        'form': form,
        'report_form': report_form,
        'is_liked': is_liked,
    })


@login_required
def delete_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    # Убедитесь, что только автор статьи может её удалить
    if article.author != request.user:
        return redirect('articles:access_denied')

    if request.method == 'POST':
        article.delete()
        return redirect('articles:article_list')

    return render(request, 'articles/delete_article.html', {'article': article})

@login_required
def create_article(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        if title and content:
            Article.objects.create(
                title=title,
                content=content,
                author=request.user
            )
            return redirect('articles:article_list')
        return render(request, 'articles/add_article.html', {'error': 'Заполните все поля!'})

    return render(request, 'articles/add_article.html')
@login_required
def edit_article(request, pk):
    article = get_object_or_404(Article, pk=pk)
    if article.author != request.user:
        return redirect('articles:access_denied')

    if request.method == 'POST':
        article.title = request.POST.get('title')
        article.content = request.POST.get('content')
        if not article.title or not article.content:
            return render(request, 'articles/edit_article.html', {'article': article, 'error': 'Заполните все поля!'})
        article.save()
        return redirect('articles:article_detail', pk=article.pk)

    return render(request, 'articles/edit_article.html', {'article': article})

def access_denied(request):
    return render(request, 'articles/access_denied.html', {})


@login_required
def delete_comment(request, pk):
    comment = get_object_or_404(Comment, pk=pk)
    if comment.author != request.user:
        return HttpResponseForbidden("Вы не можете удалить этот комментарий.")

    article_id = comment.article.pk  # Сохраняем ID статьи для перенаправления
    if request.method == 'POST':
        comment.delete()
        return redirect('articles:article_detail', pk=article_id)

    return render(request, 'articles/delete_comment.html', {'comment': comment})

@login_required
def toggle_like(request, article_id):
    article = get_object_or_404(Article, id=article_id)
    like, created = Like.objects.get_or_create(user=request.user, article=article)

    if not created:
        # Если лайк уже существует, удалить его
        like.delete()

    return redirect('articles:article_detail', pk=article.id)