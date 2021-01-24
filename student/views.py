from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from .serializers import StudentSerializer
from .models import StudentModel

class Student(APIView):
    serializer_class = StudentSerializer

    def get_queryset(self):
        student = StudentModel.objects.all()
        return student

    def get(self, request):
        student = self.get_queryset()
        serializer = StudentSerializer(student, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        serializer = StudentSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(
                serializer.errors, status=status.HTTP_400_BAD_REQUEST)



class Delete_Update_Student(APIView):
    
    serializer_class = StudentSerializer
    
    def update_object(self, pk):
            return StudentModel.objects.get(pk=pk)

    def patch(self, request, pk):
        student = self.update_object(pk)
        serializer = StudentSerializer(student, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        student = self.update_object(pk)

       
        student.delete()
        content = {
            'status': 'student Member Deleted'
        }
        return Response(content, status=status.HTTP_204_NO_CONTENT)