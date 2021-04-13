from django.shortcuts import render


def home_view(request):
    """
    Display the home page

     **Template:**
    :template:`home.html`
    """

    return render(request, 'home.html')


def legal_view(request):
    """
    Display the legal page

     **Template:**
    :template:`legal.html`
    """

    return render(request, 'legal.html')
