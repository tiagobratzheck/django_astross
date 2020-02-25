'''
Article module
'''
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from.models import Article
from.import forms

def article_home(request):
    """[Return all the articles]    
    Arguments:
        request {[http]} -- [http request]    
    Returns:
        [html] -- [template]
    """
    articles = Article.objects.all().order_by('date')
    return render(request, 'articles/article_home.html', {'articles': articles})


def article_detail(request, slug):
    """[Return the article details]    
    Arguments:
        request {[http]} -- [http request]
        slug {[string]} -- [article slug]    
    Returns:
        [html] -- [template]
    """
    article = Article.objects.get(slug=slug)
    return render(request, 'articles/article_detail.html', {'article': article})


@login_required(login_url='/accounts/login/')
def article_create(request):
    """[create a new article if the user is logged in]    
    Arguments:
        request {[http]} -- [http request]    
    Returns:
        [html] -- [article creation pages]
    """
    if request.method == 'POST':
        form = forms.CreateArticle(request.POST, request.FILES)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.author = request.user
            instance.save()
            return redirect('articles:list')
    else:
        form = forms.CreateArticle()
    return render(request, 'articles/article_create.html', {'form':form})
