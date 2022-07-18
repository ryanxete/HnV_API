from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import SuperType
from .serializers import SuperTypeSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def types(request):
    if request.method == 'GET':
        supertypes = SuperType.objects.all()
        serializer = SuperTypeSerializer(supertypes, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SuperTypeSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def types_detail(request, pk):
    type_of = get_object_or_404(SuperType, pk=pk)
    if request.method == 'GET':
        serializer = SuperTypeSerializer(type_of)
        return Response(SuperTypeSerializer.data)
    elif request.method == 'PUT':
        serializer = SuperTypeSerializer(type_of)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(SuperTypeSerializer.data)
    elif request.method == 'DELETE':
        type_of.delete()
        return Response("the item is deleted",status=status.HTTP_204_NO_CONTENT)
