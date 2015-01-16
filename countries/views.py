from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import viewsets, generics

from countries.models import Job
from countries.serializers import UserSerializer, GroupSerializer, JobSerializer

from .forms import JobForm


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer



# Create your views here.
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    
    

class JobFormView(TemplateView):
    template_name = "new.html"

    def get_context_data(self, **kwargs):
        context = super(JobFormView, self).get_context_data(**kwargs)
        context.update(JobForm=JobForm())
        return context