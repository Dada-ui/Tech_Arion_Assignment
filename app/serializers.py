from rest_framework import serializers
from app.models import *

class PipeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pipe
        fields = '__all__'