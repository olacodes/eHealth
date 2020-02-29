import sys
sys.path.append('..')

from django.contrib.auth.models import User
from rest_framework import serializers
from users.models.medical_information import(
     MedicalInformation, GENDER, 
     MARITAL_STATUS, YES_OR_NO, 
     NO_SOMETIMES_ALWAYS, COMMON_DISEASES
     )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('username', 'first_name', 'email', 'is_staff' )


class MedicalReportSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalInformation
        fields = '__all__'

class UserMedicalRecordSerializer(serializers.Serializer):
    id              = serializers.IntegerField(read_only=True)
    user            = serializers.CharField(required=True, allow_blank=False)
    age             = serializers.IntegerField(default=0)
    gender          = serializers.ChoiceField(choices=GENDER)
    marital_status  = serializers.ChoiceField(choices=MARITAL_STATUS)
    address         = serializers.CharField()
    phone_number    = serializers.CharField()
    occupation      = serializers.CharField()
    allergies       = serializers.CharField()
    last_diagnose   = serializers.CharField()
    common_illness  = serializers.ChoiceField(choices=COMMON_DISEASES)
    smoke_or_drink  = serializers.ChoiceField(choices=NO_SOMETIMES_ALWAYS)
    

    