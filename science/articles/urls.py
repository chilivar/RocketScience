from django.urls import path
from . import views

app_name = 'articles'

urlpatterns = [
    path('', views.article_list, name='article_list'),
    path('<int:pk>/', views.article_detail, name='article_detail'),
    path('add/', views.create_article, name='create_article'),
    path('<int:pk>/delete/', views.delete_article, name='delete_article'),
    path('<int:pk>/edit/', views.edit_article, name='edit_article'),
    path('access-denied/', views.access_denied, name='access_denied'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete_comment'),
    path('<int:article_id>/like/', views.toggle_like, name='toggle_like'),

]
