from django.urls import path

from mycalendar import views

urlpatterns = [
    path('', views.create_events_view, name="mycalendar"),
    path("delete/<int:id_event>", views.delete_events_view, name="delete_event")
]
