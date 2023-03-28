from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from datetime import datetime

from .models import Task

@login_required
def taskList(request):

    search = request.GET.get('search')
    if search:
        tasks = Task.objects.filter(task__icontains=search, user=request.user)
    else:
        tasks_list = Task.objects.all().order_by('-initial_date').filter(user=request.user)
        paginator = Paginator(tasks_list, 5)
        page = request.GET.get('page')
        tasks = paginator.get_page(page)

    return render(request, 'tasks/list.html', {'tasks': tasks})

@login_required
def taskView(request, id):
    task = get_object_or_404(Task, pk=id)
    return render(request, 'tasks/task.html', {'task': task})

@login_required
def newTask(request):
    if request.method=='GET':
        print('GET')
    else:
        print('POST')
        task_name = request.POST.get('task')
        task_status = request.POST.get('status')
        user_id = request.user
        print(task_name, task_status, user_id)
        Task.objects.create(task=task_name, done=task_status, user=user_id)
        return redirect('/read_all')
    return render(request, 'tasks/addtask.html')

@login_required
def editTask(request, id):
    task = get_object_or_404(Task, pk=id)
    if request.method=='GET':
        print('GET')
        print(task.task, task.initial_date)
        values = {
            'task_name': task.task,
            'task_status': task.done
        }
        return render(request, 'tasks/edittask.html', values)

    if request.method=='POST':
        print('POST')
        task_name = request.POST.get('task')
        task_status = request.POST.get('status')
        task_temp = get_object_or_404(Task, pk=id)
        temp_time_zero = datetime.now()
        if task_temp.done == 'Done' and task_status == 'Doing':
            Task.objects.filter(pk=id).update(task=task_name, done=task_status, final_date=None)
        elif task_temp.done == 'Doing' and task_status == 'Done':
            Task.objects.filter(pk=id).update(task=task_name, done=task_status, final_date=datetime.now())
        return redirect('/read_all')

@login_required
def deleteTask(request, id):
    task = get_object_or_404(Task, pk=id)
    task.delete()
    return redirect('/read_all')

@login_required
def home(request):
    return render(request, 'tasks/home.html')