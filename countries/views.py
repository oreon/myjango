from _io import BytesIO
import json

from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User, Group
from django.shortcuts import render
from django.views.generic.base import TemplateView
from rest_framework import viewsets, generics, views, status
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

from countries.models import Job
from countries.serializers import UserSerializer, GroupSerializer, JobSerializer

from .forms import JobForm
from rest_framework.permissions import AllowAny


class JobList(generics.ListCreateAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer


class JobDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Job.objects.all()
    serializer_class = JobSerializer
    
    
    
    
    
class LoginView(views.APIView):
    
    permission_classes = (AllowAny,)
    
    def post(self, request, format=None):
            
        s = str(request.DATA)
        s = s.replace("u'", "\"");
        s= s.replace("'", "\""); 
        
        print s
        
        data = json.loads(s)
        
        email = data.get('email', None)
        password = data.get('password', None)
        
        account = authenticate(username=email, password=password)
        

        if account is not None:
            #Console.write(self, " logged in " + account)
            if account.is_active:
                login(request, account)

              
                return Response("hi")
            else:
                return Response({
                    'status': 'Unauthorized',
                    'message': 'This account has been disabled.'
                }, status=status.HTTP_401_UNAUTHORIZED)
        else:
            return Response({
                'status': 'Unauthorized',
                'message': 'Username/password combination invalid.'
            }, status=status.HTTP_401_UNAUTHORIZED)


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
    template_name = "index.html"

    def get_context_data(self, **kwargs):
        context = super(JobFormView, self).get_context_data(**kwargs)
        context.update(JobForm=JobForm())
        return context