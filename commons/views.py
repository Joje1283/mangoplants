from django.shortcuts import render

from plants.models import Plant
from posts.models import Post


def index(request):
    plant_qs = Plant.objects.all()
    post_qs = Post.objects.all()
    context = {
        'plants': plant_qs,
        'posts': post_qs
    }
    return render(request, 'commons/index.html', context=context)