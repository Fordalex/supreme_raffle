from django.urls import path
from . import views

urlpatterns = [
    path("t&c", views.t_and_c_page, name="t_and_c_page"),
] 