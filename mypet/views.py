from django.shortcuts import render
from .forms import PetForm

def my_pet_view(request):
    form = PetForm()
    return render(request, "mypet.html", locals())