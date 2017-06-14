from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from .serializers import TestSerializer
from django.views.generic import TemplateView
from .models import *





class HomePageView(TemplateView):
    template_name = "index.html"


class TestViewSet(viewsets.ModelViewSet):
    
    queryset = tutorial.objects.all()
    serializer_class = TestSerializer


