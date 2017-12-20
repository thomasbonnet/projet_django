# Create your views here.
from django.shortcuts import render

from .models import Article


def index(request):
    latest_article = Article.objects.get(id=1)
    context = {
        'latest_article': latest_article,
    }
    return render(request, 'blog/index.html', context)
