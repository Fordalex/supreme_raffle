from django.urls import path
from . import views

urlpatterns = [
    path("t&c/", views.t_and_c_page, name="t_and_c_page"),
    path("privacy_policy/", views.privacy_policy_page, name="privacy_policy_page"),
] 