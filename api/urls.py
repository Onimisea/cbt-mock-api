from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.api_home),
    path("users/", include("users.urls")),
    path("quiz/", include("quiz.urls")),
]
