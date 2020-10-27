from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import * 
# Create your views here.
def index(request):
    task=Task.objects.all()
    form=TaskForm()

    if request.method=='POST':
        form=TaskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')
    context={'task':task,'form':form}
    return render(request,'task/index.html',context)

def update_task(request,pk):
    task=Task.objects.get(id=pk)

    form=TaskForm(instance=task)              #update form will be instance of task form......when we pass instance it becomes instance of task(prefield with title) and becmoes of same model
    if request.method=='POST':
        form=TaskForm(request.POST,instance=task)
        if form.is_valid():
            form.save()
            return redirect('/')


    context={'form':form}
    return render(request,'task/update_task.html',context)


def deleteTask(request,pk):
    item=Task.objects.get(id=pk)

    if request.method=='POST':
        item.delete()
        return redirect('/')
    context={'item':item}
    return render(request,'task/delete.html',context)