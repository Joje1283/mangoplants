from django.urls import path
from . import views

app_name = 'commons'

urlpatterns = [
    path('', views.index, name='home'),
]
