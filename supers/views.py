from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Super
from .serializers import SuperSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET','POST'])
def supers_list(request):
    pass