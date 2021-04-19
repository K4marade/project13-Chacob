from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .forms import EventForm

@login_required
def events_view(request):
    if request.method == "GET":
        form = EventForm()
        return render(request, "mycalendar.html", locals())