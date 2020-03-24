# -*- coding: utf-8 -*-
# # Third Party Stuff
from rest_framework import mixins, viewsets,  status
from . import models, serializers
from rest_framework.decorators import list_route, detail_route
from .models import Law, LawCategory, LawInnerCategory
from criminal_case_backend.law.serializers import LawSerializer, SubLawSerializer, SubLawCategorySerializer
# from criminal_case_backend.users.serializers import *
from criminal_case_backend.base import response
from rest_framework import generics
from rest_framework.decorators import action
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.core.exceptions import ImproperlyConfigured
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status
from django.core.mail import send_mail
import string
import random
from rest_framework.views import APIView


class LawViewSet(viewsets.ModelViewSet):

	permission_classes = (AllowAny,)
	serializer_class = serializers.LawSerializer

	def get_queryset(self):
		law_data = models.Law.objects.all()
		test = {"status":True}
		laws = []
		if law_data:
			for law in law_data:
				if law.is_active == True:
					laws.append(law)	
		test['data'] = laws
		return laws


class LawListViewSet(APIView):

	permission_classes = (AllowAny,)

	def get(self, request, format=None):
		law_data = models.Law.objects.all()
		laws = []
		if law_data:
			for law in law_data:
				if law.is_active == True:
					laws.append(law)
		serializer = LawSerializer(laws, many=True)
		return Response({'status':True, 'data':serializer.data})

class SubInnerLawViewSet(APIView):

	permission_classes = (AllowAny,)

	def get(self, request, format=None):
		law_data = models.LawInnerCategory.objects.all()
		laws = []
		if law_data:
			for law in law_data:
				if law.is_active == True:
					laws.append(law)
		serializer = SubLawCategorySerializer(laws, many=True)
		return Response({'status':True, 'data':serializer.data})



