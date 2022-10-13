from re import S
from django.shortcuts import render
from rest_framework.views import APIView
from app.models import *
from app.serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class PipeList(APIView):

    def get(self, request):
        p = self.get_object.all()
        serializer = PipeSerializer(p, many=True)
        return Response(serializer.data)

    def post(self,request):
        serializer = PipeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class PipeDetail(APIView):

    def get_object(self,pk):
        try:
            return Pipe.objects.filter(pk = pk)
        except Pipe.DoesNotExist:
            raise Response(status=status.HTTP_400_BAD_REQUEST)

    def get(self, pk, request):
        p = self.get_object(pk)
        serializer = PipeSerializer(p)
        return Response(serializer.data)

    def post(self,request):
        serializer = PipeSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self,request, pk):
        p = self.get_object(pk)
        serializer = PipeSerializer(p, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request, pk):
        p = self.get_object(pk)
        p.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)