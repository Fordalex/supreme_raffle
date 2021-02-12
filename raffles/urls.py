from django.urls import path
from . import views

urlpatterns = [
    path("", views.raffle_page, name="raffle_page"),
    path("info/<pk>/", views.raffle_info_page, name="raffle_info_page"),
] 