from django.urls import path

from mypet import views

urlpatterns = [
    path("", views.create_pet_view, name="my_pet"),
    path("edit/<int:id_pet>", views.update_pet_view, name="update_my_pet"),
    path("delete/<int:id_pet>", views.delete_pet_view, name="delete_my_pet")
]
