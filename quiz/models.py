from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from cloudinary.models import CloudinaryField
from ckeditor_uploader.fields import RichTextUploadingField

from users.models import User

# Create your models here.
class Subject(models.Model):
  subject = models.CharField(max_length=255)

  class Meta:
    verbose_name = _("Subject")
    verbose_name_plural = _("Subjects")
    ordering = ['id']

  def __str__(self):
    return self.subject


class Quiz(models.Model):
  # subject = models.ForeignKey(Subject, default=1, on_delete=models.DO_NOTHING)
  
  quiz = models.CharField(max_length=255, verbose_name=_("Quiz Title"))

  slug = models.SlugField(
    max_length=100,
    null=False,
    unique=True,
    blank=False,
    verbose_name=_("Quiz URL"),
    default=""
    )
  
  duration = models.IntegerField(default=1, verbose_name=_("Quiz Duration"))

  date_created = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name = _("Quiz")
    verbose_name_plural = _("Quizzes")
    ordering = ['id']
  
  def __str__(self):
    return self.quiz

  def get_absolute_url(self):
        return reverse("model_detail", kwargs={"slug": self.slug})


class Updated(models.Model):
  date_updated = models.DateTimeField(auto_now=True, verbose_name=_("Last Updated"))

  class Meta:
    abstract = True

class Question(Updated):
  quiz = models.ForeignKey(Quiz, related_name="question", on_delete=models.DO_NOTHING)

  question = RichTextUploadingField(verbose_name=_("Question"))

  date_created = models.DateTimeField(auto_now_add=True, verbose_name=_("Date Created"))

  is_active = models.BooleanField(default=False, verbose_name=_("Active Status"))


  class Meta:
    verbose_name = _("Question")
    verbose_name_plural = _("Questions")
    ordering = ['id']

  def __str__(self):
    return self.question


class Diagram(Updated):
  question = models.ForeignKey(Question, related_name="diagram", on_delete=models.DO_NOTHING)

  diagram = CloudinaryField(
    "Question Diagram",
    format="jpg",
    folder="QuestionDiagrams",
    default="",
    )

  class Meta:
    verbose_name = _("Diagram")
    verbose_name_plural = _("Diagrams")
    ordering = ['id']
  
  def __obj__(self):
    return self.question


class List(Updated):
  question = models.ForeignKey(Question, related_name="list", on_delete=models.DO_NOTHING)

  list = models.CharField(max_length=500, default=_("New List"), verbose_name=_("List"))

  class Meta:
    verbose_name = _("List")
    verbose_name_plural = _("Lists")
    ordering = ['id']
  
  def __str__(self):
    return self.list


class Option(Updated):
  question = models.ForeignKey(Question, related_name="option", on_delete=models.DO_NOTHING)

  option = RichTextUploadingField(verbose_name=_("Option"))

  answer = models.BooleanField(default=False, verbose_name=_("Is it correct?"))

  class Meta:
    verbose_name = _("Option")
    verbose_name_plural = _("Options")
    ordering = ['id']
  
  def __str__(self):
    return self.option

