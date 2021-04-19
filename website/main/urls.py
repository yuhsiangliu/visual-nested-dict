from django.urls import path

from . import views

urlpatterns = [
path("", views.main, name="index"),
path("v1/", views.v1, name="View 1"),
path("search/", views.search, name="Google"),
path("tree/", views.tree, name="Tree"),
path("test/", views.test, name="Test"),
]