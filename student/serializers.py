from rest_framework import serializers
from student.models import *
from django.contrib.auth.models import User
class VUZY_Serializers(serializers.ModelSerializer):
	class Meta:
		model=VUZY
		fields=('id','name','about','region','category','ort_porog','prize','examination_examples','administration','teachers')
class Administration_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Administration
		fields=('id','name','number','adress')
class Teachers_Serializers(serializers.ModelSerializer):
	class Meta:
		model=Teachers
		fields=('id','teacher_name','teacher_number','teacher_lesson','teacher_history')
class UserSerializers(serializers.ModelSerializer):
	vuzy= serializers.PrimaryKeyRelatedField(many=True, queryset=VUZY.objects.all())
	class Meta:
		model=User
		fields=('id','username','university')
class User1Serializers(serializers.ModelSerializer):
	administration = serializers.PrimaryKeyRelatedField(many=True, queryset=Administration.objects.all())
	class Meta:
		model=User
		fields=('id','username','administration')
class User2Serializers(serializers.ModelSerializer):
	teachers = serializers.PrimaryKeyRelatedField(many=True, queryset=Teachers.objects.all())
	class Meta:
		model=User
		fields=('id','username','teachers')