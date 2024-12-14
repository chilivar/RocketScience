
from django.urls import path
from . import views
from .views import logout_user
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('login', views.login, name='login'),
    path('register', views.register, name='register'),
    path('profile', views.profile, name='profile'),
    path('logout', views.logout_user, name='logout'),
    path('edit-profile', views.edit_profile, name='edit_profile')
]

