from django.shortcuts import render
from student.models import *
from student.serializers import *
from rest_framework import generics
from rest_framework.response import *
from django.http import Http404
from rest_framework.views import APIView
from student.serializers import *
from rest_framework import filters
import django_filters
from rest_framework import permissions


import re

def abc(phone_validator):
	if len(phone_validator)>13:
		return False
	result=re.findall(r'\+996\d{9}',phone_validator)
	return len(result)>0







class VUZYView(generics.ListCreateAPIView):
	queryset=VUZY.objects.all()
	serializer_class=VUZY_Serializers
	def perform_create(self,serializers):
		serializers.save(owner=self.request.user)
		
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
class AdministrationView(generics.ListCreateAPIView):
	queryset=Administration.objects.all()
	serializer_class=Administration_Serializers	
	def perform_create(self,serializers):
		serializers.save(owner=self.request.user)
		
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]
			
	def post(self,request):
		num=(request.data['number'])
		answer=abc(num) 
		if answer==True:
			serializers=Administration_Serializers(data=request.data)
			
			if serializers.is_valid():
				serializers.save()
				
			return Response('Сохранено')
		else:
			return Response('Ошибка')



class TeachersView(generics.ListCreateAPIView):
	queryset=Teachers.objects.all()
	serializer_class=Teachers_Serializers
	def perform_create(self,serializers):
		serializers.save(owner=self.request.user)
	permission_classes = [permissions.IsAuthenticatedOrReadOnly]

	def post(self,request):
		num=(request.data['number'])
		answer=abc(num) 

		if answer==True:
			
			serializers=Teachers_Serializers(data=request.data)
			if serializers.is_valid():
				serializers.save()
				
			return Response('Сохранено')
		else:
			return Response('Ошибка')

class VUZYdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=VUZY.objects.all()
	serializer_class=VUZY_Serializers


class Administrationdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Administration.objects.all()
	serializer_class=Administration_Serializers


class Teachersdetails(generics.RetrieveUpdateDestroyAPIView):
	queryset=Teachers.objects.all()
	serializer_class=Teachers_Serializers


class VUZYFindView(generics.ListAPIView):
	serializer_class = VUZY_Serializers
	queryset = VUZY.objects.all()
	filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
	filterset_fields = ['name','region','category','ort_porog','prize']


class UserList(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers


class UserDetail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = UserSerializers



class User1List(generics.ListAPIView):
    queryset = User.objects.all()
    serializer_class = User1Serializers


class User1Detail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = User1Serializers




class User2List(generics.ListAPIView):
	queryset = User.objects.all()
	serializer_class = User2Serializers


class User2Detail(generics.RetrieveAPIView):
	queryset = User.objects.all()
	serializer_class = User2Serializers