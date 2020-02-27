
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
        users = MedicalInformation.objects.select_related('user').filter(common_illness="MAL")
        serializer = UserMedicalRecordSerializer(users, many=True)
        data = serializer.data
        return Response({'users_medical_records': data}, status=status.HTTP_200_OK)

class FilterByTB(APIView):
    def get(self, response):
        users = MedicalInformation.objects.select_related('user').filter(common_illness="TUB")
        serializer = UserMedicalRecordSerializer(users, many=True)
        data = serializer.data
        return Response({'users_medical_records': data}, status=status.HTTP_200_OK)

class FilterByCholera(APIView):
    def get(self, response):
        users = MedicalInformation.objects.select_related('user').filter(common_illness="CHOL")
        serializer = UserMedicalRecordSerializer(users, many=True)
        data = serializer.data
        return Response({'users_medical_records': data}, status=status.HTTP_200_OK)