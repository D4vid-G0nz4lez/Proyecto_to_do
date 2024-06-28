from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Task(models.Model): #es una clase que hereda de models.Model, lo que la convierte en un modelo de Django.
    title= models.CharField(max_length=255) #es un campo de texto corto que almacena el título de la tarea.
    description = models.TextField() #es un campo de texto largo que almacena la descripción de la tarea.
    create_date = models.DateField(auto_now_add=True) # es un campo de fecha y hora que registra cuándo se creó la tarea. 
    task_status = models.CharField(max_length=10, default='pendiente') #es un campo de texto corto que almacena el estado de la tarea, que puede ser "pendiente" 
    
    #user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) -> str: #define cómo se representará una tarea como una cadena cuando se la imprima.
        return super().__str__()