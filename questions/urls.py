from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from django.views.generic import ListView, DetailView
from questions.models import Question


urlpatterns = [
    url(r'^$', ListView.as_view(queryset=Question.objects.all().order_by("-date")[:15],template_name="questions/questions.html")),
    url(r'^(?P<pk>\d+)$', DetailView.as_view(model = Question, template_name = "questions/question.html"))
    
]
