from django.contrib import messages
from django.shortcuts import render, redirect
from .forms import PetForm
from .models import Pet


def my_pet_view(request):
    if request.method == "GET":
        form = PetForm()
        return render(request, "mypet.html", locals())
    elif request.method == "POST":
        form = PetForm(request.POST)
        if form.is_valid():
            species = form.cleaned_data.get("species")
            gender = form.cleaned_data.get("gender")
            birth_date = form.cleaned_data.get("birth_date")
            name = form.cleaned_data.get("name")
            picture = form.cleaned_data.get("picture")

            Pet.objects.create(user=request.user,
                               species=species,
                               gender=gender,
                               birth_date=birth_date,
                               name=name,
                               picture=picture)

            messages.success(request, name + " a bien été ajouté !")
            form = PetForm()
            return redirect('my_pet')
