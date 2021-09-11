from django.urls import path
from . import views

app_name = 'posts'

urlpatterns = [
    path('', views.posts, name='posts'),
    path('<int:pk>/', views.post_detail, name='post_detail'),
    path('new/', views.post_create, name='post_create'),
    # path('<int:pk>/edit', views.post_update, name='post_update'),
    # path('<int:pk>/delete', views.post_delete, name='post_delete'),
]
