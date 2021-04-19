from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import Event

from .forms import EventForm


@login_required
def events_view(request):
    user_id = request.user
    event_list = Event.objects.filter(user_id=user_id)
    if request.method == "GET":
        form = EventForm()
        return render(request, "mycalendar.html", locals())
    elif request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get('date')
            pet_name = form.cleaned_data.get('pet_name')
            reason = form.cleaned_data.get('reason')
            comment = form.cleaned_data.get('comment')
            Event.objects.create(user_id=user_id,
                                 date=date,
                                 pet_name=pet_name,
                                 reason=reason,
                                 comment=comment)

            messages.success(request, "Votre nouveau rendez-vous a bien été enregistré")
            return render(request, "mycalendar.html", locals())