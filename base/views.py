from django.shortcuts import render
from .models import Post, Article

# Create your views here.
def home(request):
    response = 'home'
    posts = Post.objects.all().order_by('-created')
    featured_article = Article.objects.all().order_by('-created')[0]
    context = {'response':response,'posts': posts, 'featured_article' : featured_article}
    return render(request, 'base/home.html', context)

def article(request, pk):
    response = 'article'
    article = Article.objects.get(id=pk)
    context = {'response':response,'article': article}
    return render(request, 'base/article.html', context)