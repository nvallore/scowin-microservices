from django import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('student-vaccination', StudentsVaccinationViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('student-vaccination/<str:pk>', StudentsVaccinationViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
