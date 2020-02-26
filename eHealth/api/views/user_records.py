import sys
sys.path.append('..')
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User

from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models.medical_information import MedicalInformation
from ..serializers import MedicalReportSerializer, UserSerializer, UserMedicalRecordSerializer


class Users(APIView):
    def get(self, request):
        users = User.objects.all()
        serializer = UserSerializer(users, many=True)
        data = serializer.data
        return Response({'users': data}, status=status.HTTP_200_OK)


class UsersMedicalRecords(APIView):
    def get(self, response):
        users = MedicalInformation.objects.select_related('user')
        serializer = UserMedicalRecordSerializer(users, many=True)
        data = serializer.data
        return Response({'users_medical_records': data}, status=status.HTTP_200_OK)


class UserMedicalRecord(APIView):
    def get(self, request, user_id):
        user = get_object_or_404(User.objects.all(), id=user_id)
        user_medical_record = MedicalInformation.objects.filter(user_id=user.id)
        serializer = UserMedicalRecordSerializer(user_medical_record, many=True)
        data = serializer.data
        return Response({'user_medical_record': data}, status=status.HTTP_200_OK)
        
