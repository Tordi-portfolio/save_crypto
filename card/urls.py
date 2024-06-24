from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('', views.home, name='home'),
    path('send', views.send, name='send'),
    path('receive', views.receive, name='receive'),
    path('history', views.history, name='history'),
    path('swap', views.swap, name='swap'),
    path('setting', views.setting, name='setting'),   
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
]