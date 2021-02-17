from django.urls import path
from . import views

urlpatterns = [
    path("", views.view_bag, name="view_bag"),
    path("add_to_bag/<pk>", views.add_to_bag, name="add_to_bag"),
    path("empty_bag/", views.empty_bag, name="empty_bag"),
] 