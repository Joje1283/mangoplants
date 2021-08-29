from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:pk>/', views.post, name='post')
]
