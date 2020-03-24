# -*- coding: utf-8 -*-
# # Third Party Stuff
from rest_framework import mixins, viewsets,  status
from . import models, serializers
from rest_framework.decorators import list_route, detail_route
from .models import Questionnaire
from criminal_case_backend.questionnaire.serializers import QuestionnaireSerializer
from criminal_case_backend.base import response
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core.exceptions import ImproperlyConfigured
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
import string
import random
from rest_framework.views import APIView

class QuestionnaireViewSet(APIView):

	permission_classes = (AllowAny,)

	def get(self, request, format=None):
		ques_type = self.request.query_params.get('type')
		if not ques_type:
			return Response({'status':False,'msg': "This method is not allowed."}, status=status.HTTP_404_NOT_FOUND)
		ques_data = models.Questionnaire.objects.filter(ques_type=ques_type)
		serializer = []
		if ques_data:
			for ques in ques_data:
				# if ques.is_dropdown:
				# 	print("is_dropdown here")
				# 	serializer = QuestionnaireSerializer(ques_data, many=True)
				# else:
				# 	print("hello dd")
				serializer = QuestionnaireSerializer(ques_data, many=True)
		if serializer:
			return Response({'status':True, 'data':serializer.data}, status=status.HTTP_200_OK)
		else:
			return Response({'status':False,'msg': "Please contact Administrator to add content."}, status=status.HTTP_404_NOT_FOUND)