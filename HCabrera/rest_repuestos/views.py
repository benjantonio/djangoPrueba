from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from django.views.decorators.csrf import csrf_exempt
from productos.models import Repuesto
from .serializers import RepuestoSerializer

@csrf_exempt
@api_view(['GET','POST'])
def lista_repuestos(request):
    if request.method == 'GET':
        repuesto = Repuesto.objects.all()
        serializer = RepuestoSerializer(repuesto, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        data = JSONParser().parse(request)
        serializer = RepuestoSerializer(data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET','PUT','DELETE'])
def detalle_repuestos(request,id):
    try:
        repuesto = Repuesto.objects.get(idRepuesto=id)
    except Repuesto.DoesNotExist: 
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = Repuesto(repuesto)
        return Response(serializer.data)
    if request.method == 'PUT':
        data = JSONParser().parse(request)
        serializer = RepuestoSerializer(repuesto,data=data)
        if(serializer.is_valid()):
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        repuesto.delete()
        return Response(status=status.HTTP_204_NOT_CONTENT)