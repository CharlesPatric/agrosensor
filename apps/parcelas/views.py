from django.shortcuts import render
from rest_framework import viewsets
# Create your views here.
from .models import Parcela
from .serializers import ParcelaSerializer


class ParcelaViewSet(viewsets.ModelViewSet):

    queryset = Parcela.objects.all()

    serializer_class = ParcelaSerializer