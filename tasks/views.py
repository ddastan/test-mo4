from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import DetailView, CreateView

from mo4.forms import TaskFilterForm, TaskForm
from tasks.models import Task


# Create your views here.

def base(request):
    return render(request, 'tasks/base.html')

def list_tasks(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    if request.method == 'GET':
        return render(request, 'tasks/tasks.html', context)

def task_list(request):
    tasks = Task.objects.all()
    form = TaskFilterForm(request.GET)

    if form.is_valid():
        if form.cleaned_data['category']:
            tasks = tasks.filter(category=form.cleaned_data['category'])
        if form.cleaned_data['title']:
            tasks = tasks.filter(title__icontains=form.cleaned_data['title'])

    context = {
        'tasks': tasks,
        'form': form,
    }
    return render(request, 'tasks.html', context)

class TaskDetailView(DetailView):
    model = Task
    template_name = 'task_detail.html'
    context_object_name = 'task'



class TaskCreateView(CreateView):
    model = Task
    form_class = TaskForm
    template_name = 'task_form.html'
    success_url = reverse_lazy('task_list')