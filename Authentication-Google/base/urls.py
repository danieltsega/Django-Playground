from django.urls import path
from .views import index, logout_view

urlpatterns = [
    path("", index, name="home"),
    path("logout", logout_view, name="logout")
]
