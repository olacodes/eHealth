import sys
sys.path.append('..')
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from users.models.medical_information import MedicalInformation


class HealthHabit(APIView):
    def get(self, request):
        # calculate the number of those that has adequate exercise, those that doesn't and sometimes
        adequate_exercise = MedicalInformation.objects.filter(adequate_exercise='Always').count()
        no_adequate_exercise = MedicalInformation.objects.filter(adequate_exercise='No').count()
        smt_adequate_exercise = MedicalInformation.objects.filter(adequate_exercise='Sometimes').count()
        
        # calculate the number of those that has adequate sleep, those that doesn't and sometimes
        adequate_sleep = MedicalInformation.objects.filter(adequate_sleep='Always').count()
        no_adequate_sleep = MedicalInformation.objects.filter(adequate_sleep='No').count()
        smt_adequate_sleep = MedicalInformation.objects.filter(adequate_sleep='Sometimes').count()
        
        # calculate the number of those that smoke or drink or both and those that doesn't
        smoke_or_drink = MedicalInformation.objects.filter(smoke_or_drink='Always').count()
        no_smoke_or_drink = MedicalInformation.objects.filter(smoke_or_drink='No').count()
        smt_smoke_or_drink = MedicalInformation.objects.filter(smoke_or_drink='Sometimes').count()

        return Response({
            'adequate_exercise': adequate_exercise,
            'no_adequate_exercise': no_adequate_exercise,
            'smt_adequate_exercise': smt_adequate_exercise,

            'adequate_sleep': adequate_sleep,
            'no_adequate_sleep': no_adequate_sleep,
            'smt_adequate_sleep': smt_adequate_sleep,

            'smoke_or_drink': smoke_or_drink,
            'no_smoke_or_drink': no_smoke_or_drink,
            'smt_smoke_or_drink': smt_smoke_or_drink
        }, status=status.HTTP_200_OK)


class SelfMedication(APIView):
    def get(self, request):
        # calculate the total of those that practice self medication
        last_self_medication = MedicalInformation.objects.filter(last_self_medication='Yes').count()
        frequent_self_medication = MedicalInformation.objects.filter(frequent_self_medication='Yes').count()
        doctor_precription = MedicalInformation.objects.filter(doctor_precription='Yes').count()
        total_practice_self_medication = last_self_medication + frequent_self_medication + doctor_precription  
        
        # calculate the total number of those that do not practice self medication         
        no_last_self_medication = MedicalInformation.objects.filter(last_self_medication='No').count()
        no_frequent_self_medication = MedicalInformation.objects.filter(frequent_self_medication='No').count()
        no_doctor_precription = MedicalInformation.objects.filter(doctor_precription='No').count()
        total_not_practice_self_medication = no_last_self_medication + no_frequent_self_medication + no_doctor_precription  
        
        # calculate total filled forms
        total_filled_forms = total_practice_self_medication + total_not_practice_self_medication

        return Response({
            'total': total_filled_forms,
            'total_practice_self_medication': total_practice_self_medication,
            'total_not_practice_self_medication': total_not_practice_self_medication
        }, status=status.HTTP_200_OK)
       


class MostCommonIllness(APIView):
    def get(self, request):
        malaria = MedicalInformation.objects.filter(common_illness='Malaria').count()
        fever = MedicalInformation.objects.filter(common_illness='Fever').count()
        tuberculosis = MedicalInformation.objects.filter(common_illness='Tuberculosis').count()
        others = MedicalInformation.objects.filter(common_illness='Others').count()
        cholera = MedicalInformation.objects.filter(common_illness='Cholera').count()

        # Get the total of those that has filled the form
        total = malaria + fever + tuberculosis + cholera + others

        return Response({
            'total':total,
            'malaria': malaria,
            'fever': fever,
            'tuberculosis': tuberculosis,
            'cholera': cholera,
            'others': others,
        }, status=status.HTTP_200_OK)
        