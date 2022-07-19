from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def supers_list(request):
    if request.method == 'GET':
        type_name = request.query_params.get('type')
        supers = Super.objects.all()
        if type_name:
            supers = supers.filter(super_type__type=type_name)
            serializer = SuperSerializer(supers, many=True)
            return Response(serializer.data,status=status.HTTP_200_OK)    
        heroes = supers.filter(super_type__type='Hero')
        villains = supers.filter(super_type__type='Villain')
        serializer2 = SuperSerializer(heroes, many=True) 
        serializer3 = SuperSerializer(villains, many=True) 
        dictionary = {
            'heroes': serializer2.data,
            'villains': serializer3.data
        }
        return Response(dictionary, status=status.HTTP_200_OK)

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