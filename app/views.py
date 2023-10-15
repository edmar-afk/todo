from django.shortcuts import render, redirect
from datetime import datetime
from .models import Tasks
from django.contrib import messages

# Create your views here.

def homepage(request):
    today = datetime.now()
    tasks = Tasks.objects.all().order_by('-id')
    
    if request.method == 'POST':
        task = request.POST['task']
        date =  request.POST['date']
        
        new_task = Tasks(task=task, date=date)
        new_task.save()
        messages.success(request, 'Task Added!')
        return redirect('/homepage') 
    
    context = {
        'today' : today,
        'tasks' : tasks,
    }
    return render(request, 'index.html', context)


def deletetask(request, task_id):
    Tasks.objects.filter(id=task_id).delete()
    messages.error(request, 'Task Deleted')
    return redirect('/homepage') 