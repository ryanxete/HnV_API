from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        supers = Super.objects.all()
        serializer = SuperSerializer(supers, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = SuperSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
@api_view(['GET','PUT','DELETE'])
def supers_detail(request, pk):
    the_one = get_object_or_404(Super, pk=pk)
    if request.method == 'GET':
        serializer = SuperSerializer(the_one)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = SuperSerializer(the_one,data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    elif request.method == 'DELETE':
        the_one.delete()
        return Response("the item is deleted",status=status.HTTP_204_NO_CONTENT)