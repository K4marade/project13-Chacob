from django.urls import path

from mypet import views

urlpatterns = [
    path("", views.my_pet_view, name="my_pet")
]