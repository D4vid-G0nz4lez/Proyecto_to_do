from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.task_list, name='task_list'),  # URL para mostrar la lista de tareas
    path('create/', views.create_task, name='create_task'),  # URL para crear una nueva tarea
    path('edit/<int:task_id>/', views.edit_task, name='edit_task'),  # URL para editar una tarea existente
    path('delete/<int:task_id>/', views.delete_task, name='delete_task'),  # URL para eliminar una tarea
]