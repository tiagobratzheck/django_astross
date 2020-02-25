from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout

# Create your views here.


def signup_view(request):
    """[Sign up function]
    Arguments:
        request {[http]} -- [http request]
    Returns:
        [html] -- [html articles or signup form]
    """
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()            
            login(request, user)
            return redirect('articles:list')
    else:
        form = UserCreationForm()
    return render(request, 'accounts/signup.html', {'form': form})


def login_view(request):
    """[login function]
    Arguments:
        request {[http]} -- [http request]
    Returns:
        [html] -- [html articles or login form]
    """
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('articles:list')
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})


def logout_view(request):
    """[logout function]    
    Arguments:
        request {[http]} -- [http request]    
    Returns:
        [html] -- [The articles list]
    """
    if request.method == 'POST':
        logout(request)
    return redirect('articles:list')
