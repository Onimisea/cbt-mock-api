from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.quiz_home),
    path("all/", views.all_quizzes.as_view(),),
    path("<str:slug>/", views.Quiz.as_view(),),
]
