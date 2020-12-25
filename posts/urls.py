from django.urls import path, include
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.index, name='index'),
    path('write/', views.write, name='write'),
    path('detail/<int:pk>/', views.detail, name='detail'),
    path('update/<int:pk>/', views.update, name='update'),
    path('delete/<int:pk>/', views.delete, name='delete'),
    path('alldelete', views.AllDelete, name='alldelete'),
]
