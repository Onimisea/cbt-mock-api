from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.quiz_home),
    path("all/", views.all_quizzes.as_view(),),
    path("all/questions/", views.all_questions.as_view(),),
    path("<str:slug>/", views.Quiz.as_view(),),
]
