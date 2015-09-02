from django.conf.urls import include, url
from django.contrib import admin
from student import views
urlpatterns = [
    
    url(r'^student/$', views.StudentList.as_view()),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),    
    url(r'^bus/$', views.BusList.as_view()),
    url(r'^bus/(?P<pk>[0-9]+)/$', views.BusDetail.as_view()),
    url(r'^activity/$', views.ActivityList.as_view()),
    url(r'^activity/(?P<pk>[0-9]+)/$', views.ActivityDetail.as_view()),
]
