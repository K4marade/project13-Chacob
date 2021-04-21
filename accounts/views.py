from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import logout, login, authenticate
from .forms import RegisterForm

# from .decorators import unauthenticated_user


# @unauthenticated_user
def register_view(request):
    """
    GET method:
    Displays the register page

     **Template:**
    :template:`registration/register.html`

    POST method:
    Redirects to home page

     **Template:**
     :template: `home/home.html`
    """

    if request.method == "GET":
        form = RegisterForm()
        return render(request, 'registration/register.html', locals())
    elif request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            messages.success(request, "Bienvenue " + username + " !")
            return redirect('home')


def logout_view(request):
    """
    Disconnect the user and redirect to the homepage

     **Template:**
    :template:`home/home.html`

    """
    logout(request)
    messages.info(request, "Vous êtes bien déconnecté")
    return redirect('home')


@login_required
def profile_view(request):
    """
    Display the user profile page is user is authenticated

    **Template:**
    :template:`account/profile.html`
    """

    return render(request, 'account/profile.html', locals())
