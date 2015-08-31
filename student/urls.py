from django.conf.urls import include, url
from django.contrib import admin
from student import views
urlpatterns = [
    
    url(r'^student/$', views.StudentList.as_view()),
    url(r'^student/(?P<pk>[0-9]+)/$', views.StudentDetail.as_view()),    
    url(r'^travel/$', views.TravelList.as_view()),
    url(r'^travel/(?P<pk>[0-9]+)/$', views.TravelDetail.as_view()),
]
