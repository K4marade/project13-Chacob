from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import AddPetForm, EditPetForm
from .models import Pet


def create_pet_view(request):
    pets_list = Pet.objects.filter(user=request.user).order_by('species')

    if request.method == "GET":
        form = AddPetForm()
    elif request.method == "POST":
        form = AddPetForm(request.POST, request.FILES)
        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            messages.success(request, pet.name + " a bien été ajouté !")
            form = AddPetForm()
            return redirect('mypet')
    return render(request, "mypet.html", locals())

    # else:
    #     error = form.errors
    #     form = AddPetForm(request.POST or None, request.FILES or None)
    #     return render(request, "mypet.html", locals())


def update_pet_view(request, id_pet):
    instance_pet = Pet.objects.get(pk=id_pet)
    if request.method == "GET":
        form = EditPetForm(instance=instance_pet)
    elif request.method == "POST":
        form = EditPetForm(request.POST, request.FILES, instance=instance_pet)

        if form.is_valid():
            pet = form.save(commit=False)
            pet.user = request.user
            pet.save()
            return redirect("mypet")
        # else:
        #     error = form.errors
        #     return render(request, "mypet.html", locals())
    return render(request, 'update_my_pet.html', locals())


def delete_pet_view(request, id_pet):
    instance_pet = Pet.objects.get(pk=id_pet)
    instance_pet.delete()
    return redirect("mypet")
