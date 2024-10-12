from django.urls import path,include
from . import views

urlpatterns = [
    path('todos', views.TodoListCreate.as_view(),name='note_list'),
    path('',views.home),
    path('todos/delete/<int:pk>/', views.TodoDelete.as_view(),name='note_delete'),
   
]