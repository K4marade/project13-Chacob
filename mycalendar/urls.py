from django.urls import path

from mycalendar import views

urlpatterns = [
    path('', views.events_view, name="events"),
]
