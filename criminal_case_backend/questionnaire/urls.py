from django.conf.urls import include, url
from django.contrib.auth import views as auth_views
from django.views.generic import TemplateView
from . import views
from . import api
from criminal_case_backend.questionnaire.api import *
        
urlpatterns = [
    url(r'^questionnaire/$', QuestionnaireViewSet.as_view()),
]
