from django.shortcuts import render

# myapp/views.py
from rest_framework import viewsets
from .models import Term, PriceList
from .serializers import TermSerializer, PriceListSerializer

class TermViewSet(viewsets.ModelViewSet):
    queryset = Term.objects.all()
    serializer_class = TermSerializer

class PriceListViewSet(viewsets.ModelViewSet):
    #for fetching data in order asc
    queryset = PriceList.objects.all().order_by('id')
    serializer_class = PriceListSerializer
    ordering_fields = ['id']
