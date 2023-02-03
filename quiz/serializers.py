from rest_framework import serializers
from .models import Quiz, Question, Diagram, List, Option


class QuizSerializer(serializers.ModelSerializer):
  # duration = serializers.IntegerRelatedField

  class Meta:
    model = Quiz
    fields = ['id', 'quiz', 'slug', 'duration', ]

class DiagramSerializer(serializers.ModelSerializer):
  # question = serializers.StringRelatedField()
  
  class Meta:
    model = Diagram
    fields = ['id', 'diagram']

class ListSerializer(serializers.ModelSerializer):
  # question = serializers.StringRelatedField()
  
  class Meta:
    model = List
    fields = ['id', 'list']

class OptionSerializer(serializers.ModelSerializer):
  # question = serializers.StringRelatedField()
  
  class Meta:
    model = Option
    fields = ['id', 'option', 'answer']


class QuestionSerializer(serializers.ModelSerializer):
  quiz = serializers.StringRelatedField()
  diagram = DiagramSerializer(many=True)
  list = ListSerializer(many=True)
  option = OptionSerializer(many=True)
  
  class Meta:
    model = Question
    fields = ['id', 'quiz', 'question', 'diagram', 'list', 'option', 'is_active']
