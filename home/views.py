from django.shortcuts import render


def home_view(request):
    """
    Display the home page

     **Template:**
    :template:`home.html`
    """

    return render(request, 'home.html')