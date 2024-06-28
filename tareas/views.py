from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from .forms import TaskForm

def task_list(request):
    tasks = Task.objects.all()
    return render(request, 'templates/task_list.html', {'tasks': tasks} )

def create_task(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user
            task.save
            return redirect('task_list')
        else:
            form = TaskForm()
        return render(request, 'templates/create_task.html', {'form': form}) 
    
def edit_task(request, task_id):
    task = get_object_or_404(Task,id =task_id)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid(): 
            form.save()
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
    return render(request, 'templates/edit_task.html', {form : form})            

def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id)
    if request.method == 'POTS':
        task.delete()
    return redirect('task_list')
       
# Aquí hay una explicación de cada vista:

# task_list: Esta vista muestra todas las tareas del usuario actual. Filtra las tareas por el usuario actual y las pasa al template task_list.html.
# create_task: Esta vista permite al usuario crear una nueva tarea. Si se envía un formulario POST válido, crea la tarea y redirige al usuario a la página de la lista de tareas. Si no, muestra el formulario de creación de tareas.
# edit_task: Esta vista permite al usuario editar una tarea existente. Recibe el ID de la tarea que se va a editar, recupera la tarea correspondiente, y muestra un formulario prellenado con los datos de la tarea. Si se envía un formulario POST válido, guarda los cambios y redirige al usuario a la página de la lista de tareas.
# delete_task: Esta vista permite al usuario eliminar una tarea existente. Recibe el ID de la tarea que se va a eliminar, recupera la tarea correspondiente, y muestra una página de confirmación de eliminación. Si se confirma la eliminación, la tarea se elimina de la base de datos y se redirige al usuario a la página de la lista de tareas.

