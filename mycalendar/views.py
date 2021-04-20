from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from accounts.models import UserAuth
from .models import Event
from django.core.mail import send_mail

from .forms import EventForm

import environ

env = environ.Env()
environ.Env.read_env()


@login_required
def events_view(request):
    current_user = request.user

    event_list = Event.objects.filter(user_id=current_user)
    if request.method == "GET":
        form = EventForm()
        return render(request, "mycalendar.html", locals())
    elif request.method == "POST":
        form = EventForm(request.POST)
        if form.is_valid():
            date = form.cleaned_data.get("date")
            pet_name = form.cleaned_data.get("pet_name")
            reason = form.cleaned_data.get("reason")
            comment = form.cleaned_data.get("comment")
            alert = form.cleaned_data.get("mail_alert")

            Event.objects.create(user_id=current_user,
                                 date=date,
                                 pet_name=pet_name,
                                 reason=reason,
                                 comment=comment,
                                 mail_alert=alert)

            if alert is True:
                user_email = UserAuth.objects.get(id=current_user.id).email
                send_mail("Rappel de rendez-vous vétérinaire",
                          "Bonjour,\n\nNous vous rappelons que vous avez rendez-vous aujourd'hui "
                          "pour " + pet_name + ".\n\n"
                          "Motif : " + reason,
                          env("GMAIL_USER"),
                          [user_email])

            messages.success(request, "Votre nouveau rendez-vous a bien été enregistré")
            form = EventForm()
            return render(request, "mycalendar.html", locals())
