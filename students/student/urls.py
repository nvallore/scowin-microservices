from django import views
from django.urls import path, include
from .views import *

urlpatterns = [
    path('students', StudentsViewSet.as_view({
        'get': 'list',
        'post': 'create'
    })),
    path('students/<str:pk>', StudentsViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }))
]
