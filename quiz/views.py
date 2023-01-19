from django.shortcuts import get_object_or_404
from rest_framework import generics, status
from rest_framework.decorators import APIView, api_view
from rest_framework.permissions import (
    AllowAny,
    IsAdminUser,
    IsAuthenticated,
    IsAuthenticatedOrReadOnly,
)
from rest_framework.request import Request
from rest_framework.response import Response


from .models import Quiz
from .serializers import QuizSerializer

# from django.contrib.auth import get_user_model


@api_view(["GET"])
def quiz_home(request, *args, **kwargs):
    # DRF API View

    return Response({"CBT MOCK": "Welcome to our Quiz Home"}, status=200)


class all_quizzes(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class Quiz(APIView):
    def get(self, request, format=None, *args, **kwargs):
        quiz = Quiz.objects.filter(quiz__quiz=kwargs['slug']).order_by('quiz_id')

        serializer = QuizSerializer(quiz)

        return Response(serializer.data)