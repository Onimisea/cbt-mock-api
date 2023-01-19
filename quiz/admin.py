from django.contrib import admin
from . import models

# Register your models here.

@admin.register(models.Subject)
class SubjectAdmin(admin.ModelAdmin):
  list_display = [
    'subject',
  ]

@admin.register(models.Quiz)
class QuizAdmin(admin.ModelAdmin):
  list_display = [
    'quiz', 'subject'
  ]
  prepopulated_fields = {"slug": ("quiz",)}

class DiagramInlineModel(admin.TabularInline):
  model = models.Diagram
  fields = ['diagram',]

class ListInlineModel(admin.TabularInline):
  model = models.List
  fields = ['list',]

class OptionInlineModel(admin.TabularInline):
  model = models.Option
  fields = ['option', 'is_correct',]

@admin.register(models.Question)
class QuestionAdmin(admin.ModelAdmin):
  fields = [
    'quiz', 'question',
  ]

  list_display = [
    'quiz', 'question', 'date_updated'
  ]

  inlines = [OptionInlineModel,]

@admin.register(models.Diagram)
class DiagramAdmin(admin.ModelAdmin):
  list_display = ['diagram', 'question',]

@admin.register(models.List)
class ListAdmin(admin.ModelAdmin):
  list_display = ['list', 'question',]

@admin.register(models.Option)
class OptionAdmin(admin.ModelAdmin):
  list_display = ['option', 'is_correct', 'question',]