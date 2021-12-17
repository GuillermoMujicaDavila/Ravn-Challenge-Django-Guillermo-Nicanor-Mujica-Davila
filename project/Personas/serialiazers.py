from rest_framework import serializers
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
from .models import PersonModel


class PersonSerializer(serializers.ModelSerializer):
    personId = serializers.IntegerField()
    personName = serializers.CharField()
    personEye = serializers.CharField()
    personHair = serializers.CharField()
    personSkin = serializers.CharField()
    personBirth = serializers.CharField()
    personType = serializers.CharField()
    personHouse= serializers.CharField()
    class Meta:
        model= PersonModel 
        
        fields='__all__'
        extra_kwargs= {
            'personModel':{
            'write_only': True,    
            }
        }
    