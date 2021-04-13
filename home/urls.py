from django.urls import path
from home import views

urlpatterns = [
    path('', views.home_view, name="home"),
    path('legal/', views.legal_view, name="legal"),

]
