from django.shortcuts import render, redirect
from django.http import HttpResponseNotAllowed
from .forms import UserForm
from django.conf import settings
from django.core.files.storage import FileSystemStorage

users = ['Вася Питонов', 'Петя Гадюкин']



def index(request):
    context = {
        'users': users
    }
    return render(request, 'app/index.html', context)


def add(request):
    if request.method == 'GET':
        form_fields = UserForm()
        context = {
            'form_fields': form_fields
        }
        return render(request, 'app/add.html', context)
    elif request.method == 'POST':
        form_fields = UserForm(request.POST, request.FILES)
        if form_fields.is_valid():
            file = request.FILES['file']
            file_system = FileSystemStorage()
            file_name = file_system.save(file.name, file)
            file_url = file_system.url(file_name)
            context = {
                'url': file_url

            }
            return render(request, 'app/download.html', context)
        else:
            return render(request, 'app/add.html', context)
    else:
        return HttpResponseNotAllowed(
            ['POST', 'GET'],
            content='Ошибка Этот метод не разрешен!'
        )
