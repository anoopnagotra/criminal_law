from django.db import models
from django.core import serializers
from criminal_case_backend.users.models import User
import datetime
import uuid

Questionaire_Type = (
        ('accused', 'accused'),
        ('victim', 'victim'),
        ('offence', 'offence')
    )

class QuestionnaireType(models.Model):
    q_type = models.CharField(max_length=250, blank=False, unique=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at =models.DateTimeField(auto_now=True, editable=False)

    class Meta:
         db_table = "questionaire_type"
         verbose_name_plural = "Questionnaire Type"
    
    def __str__(self):
        return self.q_type

class Questionnaire(models.Model):
    name = models.CharField(max_length=350,blank=False,unique=True)
    ques_type = models.CharField(max_length=120, null=False, blank=False, choices=Questionaire_Type, help_text='Questionnaire Type')
    is_active = models.BooleanField(default=False)
    is_dropdown = models.BooleanField(default=False)
    # answer = models.CharField(max_length=120, null=False, blank=False,help_text='Yes/No')
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at =models.DateTimeField(auto_now=True, editable=False)

    class Meta:
         db_table = "questionnaires"
         verbose_name_plural = "Questionnaire"
    
    def __str__(self):
        return self.name

import calendar
AGE_CHOICE = [(str(i), str(i)) for i in range(1,101)]
MONTH_CHOICE = [(str(i), calendar.month_name[i]) for i in range(1,13)]

class Age(models.Model):
    age = models.CharField(choices=MONTH_CHOICE, max_length=250, blank=False, unique=False)
    is_active = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at =models.DateTimeField(auto_now=True, editable=False)

    class Meta:
         db_table = "age_group"
         verbose_name_plural = "Age Group"
    
    def __str__(self):
        return self.age

# class Month(models.Model):
#     age = models.CharField(choices=MONTH_CHOICE, max_length=250, blank=False, unique=False)
#     is_active = models.BooleanField(default=False)
#     created_at = models.DateTimeField(auto_now_add=True, editable=False)
#     updated_at =models.DateTimeField(auto_now=True, editable=False)

#     class Meta:
#          db_table = "age_group"
#          verbose_name_plural = "Age Group"
    
#     def __str__(self):
#         return self.age

class QuesAnswer(models.Model):
    ques = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
    answer = models.CharField(max_length=350,blank=True,unique=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at =models.DateTimeField(auto_now=True, editable=False)

    class Meta:
         db_table = "questionnaire_answers"
         verbose_name_plural = "Questionnaire Options"
    
    def __str__(self):
        return self.answer