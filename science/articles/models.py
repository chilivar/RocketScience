from django.contrib.auth.models import User
from django.db import models  # Не забудьте импортировать models!

class Article(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User

class Comment(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='comments')  # Связь с Article
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')  # Автор комментария
    content = models.TextField()  # Текст комментария
    created_at = models.DateTimeField(auto_now_add=True)  # Дата создания
    updated_at = models.DateTimeField(auto_now=True)  # Дата последнего изменения

    def __str__(self):
        return f'Комментарий от {self.author} на "{self.article.title}"'

from django.db import models
from django.contrib.auth.models import User

class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='likes')
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ('user', 'article')  # Уникальность: один пользователь может лайкнуть одну статью только один раз

    def __str__(self):
        return f'{self.user.username} лайкнул {self.article.title}'

class Report(models.Model):
    article = models.ForeignKey('Article', on_delete=models.CASCADE, related_name='reports')  # Статья, на которую подали жалобу
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reports')  # Пользователь, подавший жалобу
    reason = models.TextField()  # Причина жалобы
    created_at = models.DateTimeField(auto_now_add=True)  # Дата подачи жалобы

    def __str__(self):
        return f'Жалоба от {self.user.username} на статью "{self.article.title}"'