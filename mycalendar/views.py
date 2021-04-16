from django.shortcuts import render
from .forms import EventForm


def events_view(request):
    form = EventForm()
    return render(request, "mycalendar.html", locals())
