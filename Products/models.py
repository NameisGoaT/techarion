from django.db import models
import uuid

# import pkgutil
# from django.shortcuts import render
# from rest_framework.response import Response
# from .models import *
# from .serializers import *
# from rest_framework import status, viewsets




class Product(models.Model):
    title=models.CharField(max_length=100)
    description=models.TextField(blank=True)
    unique_id=models.UUIDField(primary_key = True,default = uuid.uuid4,editable = False)
    price=models.IntegerField()

class ProductImage(models.Model):
    product=models.ForeignKey(Product)
    image=models.ImageField(blank=True)

 

        
    


















class Studentviewset(viewsets.ViewSet):
    def list(self,request):
        queryset=Student.objects.all()
        serializer=StudentSerializer(queryset,many=True)
        return Response(serializer.data)
    
    def retrieve(self,request,pk=None):
        id=pk
        if id is not None:
            queryset=Student.objects.get(id=id)
            serializer=StudentSerializer(queryset)
            return Response(serializer.data)
    
    def update(self,request,pk):
        id=pk
        queryset=Student.objects.get(pk=id)
        serializer=StudentSerializer(queryset,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'MSG':'Complete data updated'})
        return Response(serializer.error,status=status.HTTP_404_BAD_REQUEST)

    def destroy(self,request):
        id=pk
        queryset=Student.objects.get(pk=id)
        queryset.delete()
        return Response({'msg':'Deleted'})
    
    def create(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'complete data created'})
        return Response(serializer.error,status=status.HTTP_404_BAD_REQUEST)
        

