import sys
sys.path.append('..')
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models.medical_information import MedicalInformation
from ..serializers import (
    MedicalReportSerializer, 
    UserSerializer, 
    UserMedicalRecordSerializer
    )

# filter users based on their most recent illness
# marital status
# gender

class FilterByMalaria(APIView):
    def get(self, response):
        users = MedicalInformation.objects.select_related('user').filter(common_illness="Malaria")
        serializer = UserMedicalRecordSerializer(users, many=True)
        data = serializer.data
        return Response({'malaria': data}, status=status.HTTP_200_OK)

class FilterByTB(APIView):
    def get(self, response):
        users = MedicalInformation.objects.select_related('user').filter(common_illness="Tuberculosis")
        serializer = UserMedicalRecordSerializer(users, many=True)
        data = serializer.data
        return Response({'tuberculosis': data}, status=status.HTTP_200_OK)

class FilterByCholera(APIView):
    def get(self, response):
        users = MedicalInformation.objects.select_related('user').filter(common_illness="Cholera")
        serializer = UserMedicalRecordSerializer(users, many=True)
        data = serializer.data
        return Response({'choler': data}, status=status.HTTP_200_OK)

class FilterByFever(APIView):
    def get(self, response):
        users = MedicalInformation.objects.select_related('user').filter(common_illness="Fever")
        serializer = UserMedicalRecordSerializer(users, many=True)
        data = serializer.data
        return Response({'fever': data}, status=status.HTTP_200_OK)
