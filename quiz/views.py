import random
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

from users.models import User
from .models import Quiz, Question
from .serializers import QuizSerializer, QuestionSerializer

# from django.contrib.auth import get_user_model


@api_view(["GET"])
def quiz_home(request, *args, **kwargs):
    # DRF API View

    return Response({"CBT MOCK": "Welcome to our Quiz Home"}, status=200)


class all_quizzes(generics.ListAPIView):
    serializer_class = QuizSerializer
    queryset = Quiz.objects.all()


class Quiz(APIView):
    # queryset = Quiz.objects.all()
    # serializer_class = QuizSerializer
    # lookup_field = 'slug'


    def get(self, request, slug, *args, **kwargs):
        queryset = Question.objects.all().filter(quiz__slug=slug)
        print(queryset)
        serializer = QuestionSerializer(queryset, many=True)
        response = random.sample(serializer.data, len(serializer.data))
        return Response(data=response, status=status.HTTP_200_OK)

