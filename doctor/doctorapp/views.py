from django.shortcuts import render
from rest_framework import viewsets 
from rest_framework.views import APIView
from doctorapp.serializers import DoctorSerializer,PatientSerializer
from doctorapp.models import doctor,patient
import traceback
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

class DocotorView(APIView):
    def post(self,request):
        try:
            data=request.data
            data["name"]=str(data["name"]).title()
            print(data)
            serializer = DoctorSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response({"doctor" : serializer.data},status=status.HTTP_201_CREATED)
            
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            traceback.print_exc()
    
    def get(self,request):
        try:
            data=doctor.objects.all()
            ser=DoctorSerializer(data,many=True)
            return Response(ser.data,status=status.HTTP_200_OK)
        except Exception as e:
            traceback.print_exc()



class PatientViewSet(viewsets.ModelViewSet):
    queryset = patient.objects.all()
    serializer_class = PatientSerializer