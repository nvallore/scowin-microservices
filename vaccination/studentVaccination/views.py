from django.shortcuts import render
from .models import StudentVaccination
from .serializers import StudentVaccinationSerializer
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework import viewsets, status
from .producer import publish

class StudentsVaccinationViewSet(viewsets.ViewSet):
    def list(self, request):
        students = StudentVaccination.objects.all()
        serializer = StudentVaccinationSerializer(students, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StudentVaccinationSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('student_vaccinated', serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        student = StudentVaccination.objects.get(id=pk)
        serializer = StudentVaccinationSerializer(student)
        return Response(serializer.data)

    def update(self, request, pk=None):
        student = StudentVaccination.objects.get(id=pk)
        serializer = StudentVaccinationSerializer(instance=student, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        publish('product_updated', serializer.data)
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)

    def destroy(self, request, pk=None):
        student = StudentVaccination.objects.get(id=pk)
        StudentVaccination.delete()
        publish('product_deleted', pk)
        return Response(status=status.HTTP_204_NO_CONTENT)

