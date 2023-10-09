from django.urls import path

from . import views

urlpatterns = [
    path('demo',views.demo,name='demo'),
    path('register', views.register, name='register'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('application', views.application, name='application'),
    path('new', views.newpage, name='newpage')
]