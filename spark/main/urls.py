from django.urls import path
from . import views

urlpatterns = [
    path("news", views.index00, name = "index00"),
    path("", views.index11, name = "index11"),
    path("career", views.index22, name = "index22"),
    path("about-us", views.index33, name = "index33"),
    path("tickets", views.index44, name = "index44"),
]
