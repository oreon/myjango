from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.contrib.auth.decorators import login_required
from rest_framework import routers

from countries import views
from countries.views import JobFormView


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
      url(r'^job/$', views.JobList.as_view()),
    url(r'^job/(?P<pk>[0-9]+)/$', views.JobDetail.as_view()),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^job-form/$',login_required(JobFormView.as_view()), name='job_form')
]