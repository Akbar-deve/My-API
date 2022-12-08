from rest_framework import serializers
from doctorapp.models import doctor,patient

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = doctor
        fields = ('name','specialization','qualification')

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = patient
        fields = ('name','birth_year','age','gender','doctor')