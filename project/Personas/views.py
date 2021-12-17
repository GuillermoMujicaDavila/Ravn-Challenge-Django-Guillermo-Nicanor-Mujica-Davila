from django.core.checks.messages import Error
from django.db.models import query
from django.shortcuts import render
from rest_framework.exceptions import ErrorDetail
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.generics import GenericAPIView, RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView,ListAPIView

from .serialiazers import PersonSerializer
from .models import  PersonModel

# Create your views here.

class PersonController(RetrieveUpdateDestroyAPIView): 
    serializer_class = PersonSerializer
    def get(self,request,id):    
        try:
            respuesta =PersonModel.objects.get(personId = id)
            print (respuesta)
        
            if respuesta is None:
                return Response(
                    data={
                        "message":"Adopcion no encontrada",
                        "content":None
                    }, status= 404
                )
            respuesta_serealizada = PersonSerializer(instance=respuesta)
            return Response(data={
            "message":"Persona encontrada",
            "content": respuesta_serealizada.data
            }, status=200)
        except PersonModel.DoesNotExist:
            print('No se encontro')
            return Response(data={
            "message":"Error Bad Query",
            "content": None
            }, status=400)
    
   
    
class PeopleController(ListAPIView):
    queryset = PersonModel.objects.all() 
    serializer_class = PersonSerializer
    def get(self,request):
        try:
            respuesta = self.get_queryset()
            print (respuesta)
            respuesta_serializada = self.serializer_class(
                instance=respuesta, many=True
            )
            if len(respuesta) == 0:
                return Response(data={'message':'Sin data',
                                      'data':None},status=404)
                
            else:
                return Response(data={'message': 'repuesta exitosa',
                                'data': respuesta_serializada.data},status=200)
        except:
            return Response(data={'message': 'error en el query',
                                   'data': None},status=400)       
            
            
        
    

