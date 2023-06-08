from django.shortcuts import render, redirect
from .models import Task
from .forms import Todoform

# Create your views here.


def demo(request):
    task1 = Task.objects.all()
    if request.method=='POST':
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date')
        task=Task(name=name,priority=priority,date=date)
        task.save()

    return render(request,'index.html',{'task1':task1})

def delete(request,task_id):
    task=Task.objects.get(id=task_id)
    if request.method == 'POST':
        task.delete()
        return redirect('/')
    return render(request,'delete.html')


def update(request,id):
    task=Task.objects.get(id=id)
    f=Todoform(request.POST or None, instance=task)
    if f.is_valid():
        f.save()
        return redirect('/')
    return render(request,'edit.html',{'f':f,'task':task})