from django.shortcuts import render
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny
from django.contrib.auth.models import User
from .models import Todo
from .serializers import *

def home(request):
    return render(request,'app/base.html')
class CreateUserView(generics.CreateAPIView):
    queryset=User.objects.all()
    serializer_class=UserSerialized
    permission_classes = [AllowAny]

class TodoListCreate(generics.ListCreateAPIView):
    queryset=User.objects.all()
    serializer_class=TodoSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        user=self.request.user
        return Todo.objects.filter(author=user)
        
    def perform_create(self, serializer):
       if serializer.is_valid():
           serializer.save(author=self.request.user)
       else:
           print(serializer.errors)

class TodoDelete(generics.DestroyAPIView):
    serializer_class=TodoSerializer
    permission_classes=[IsAuthenticated]
    
    def get_queryset(self):
        user=self.request.user
        return Todo.objects.filter(author=user)
        
    
    