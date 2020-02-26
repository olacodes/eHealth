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
        adequate_exercise = MedicalInformation.objects.filter(adequate_exercise='AWS').count()
        no_adequate_exercise = MedicalInformation.objects.filter(adequate_exercise='NO').count()
        smt_adequate_exercise = MedicalInformation.objects.filter(adequate_exercise='SMT').count()
        
        # calculate the number of those that has adequate sleep, those that doesn't and sometimes
        adequate_sleep = MedicalInformation.objects.filter(adequate_sleep='AWS').count()
        no_adequate_sleep = MedicalInformation.objects.filter(adequate_sleep='NO').count()
        smt_adequate_sleep = MedicalInformation.objects.filter(adequate_sleep='SMT').count()
        
        # calculate the number of those that smoke or drink or both and those that doesn't
        smoke_or_drink = MedicalInformation.objects.filter(smoke_or_drink='AWS').count()
        no_smoke_or_drink = MedicalInformation.objects.filter(smoke_or_drink='NO').count()
        smt_smoke_or_drink = MedicalInformation.objects.filter(smoke_or_drink='SMT').count()

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
        last_self_medication = MedicalInformation.objects.filter(last_self_medication='Y').count()
        frequent_self_medication = MedicalInformation.objects.filter(frequent_self_medication='Y').count()
        doctor_precription = MedicalInformation.objects.filter(doctor_precription='Y').count()
        total_practice_self_medication = last_self_medication + frequent_self_medication + doctor_precription  
        
        # calculate the total number of those that do not practice self medication         
        no_last_self_medication = MedicalInformation.objects.filter(last_self_medication='N').count()
        no_frequent_self_medication = MedicalInformation.objects.filter(frequent_self_medication='N').count()
        no_doctor_precription = MedicalInformation.objects.filter(doctor_precription='N').count()
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
        total_form = MedicalInformation.objects.all().count()
        empty_fields = MedicalInformation.objects.filter(common_illness='').count()
        malaria = MedicalInformation.objects.filter(common_illness='MAL').count()
        fever = MedicalInformation.objects.filter(common_illness='FEV').count()
        tuberculosis = MedicalInformation.objects.filter(common_illness='TUB').count()
        others = MedicalInformation.objects.filter(common_illness='OTHERS').count()
        cholera = MedicalInformation.objects.filter(common_illness='CHL').count()

        # Get the total of those that has filled the form
        total = total_form - empty_fields 

        return Response({
            'total':total,
            'empty_fields': empty_fields,
            'malaria': malaria,
            'fever': fever,
            'tuberculosis': tuberculosis,
            'cholera': cholera,
            'others': others,
        }, status=status.HTTP_200_OK)