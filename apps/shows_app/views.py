from django.shortcuts import render, redirect
from .models import Shows
from django.contrib import messages

def index(request):
    context = {
        'shows_list': Shows.objects.all(),
    }
    return render(request, 'shows_app/index.html', context)

def new(request):
    return render(request, 'shows_app/new.html')

def create(request):
    errors = Shows.objects.validate(request.POST)
    if errors:
        for key, value in errors.items():
            messages.error(request, {key: value})      
        return render(request, 'shows_app/new.html')
    if request.method == "POST":
        id = Shows.objects.add(request.POST)
    return redirect(f'/shows/{id}')

def show(request, id):
    values = Shows.objects.display(id)
    context = {
        'id': values.id,
        'title': values.title,
        'network': values.network,
        'release': values.release,
        'description': values.description,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
    }
    return render(request, 'shows_app/show.html', context)

def edit(request, id):
    values = Shows.objects.display(id)
    context = {
        'id': values.id,
        'title': values.title,
        'network': values.network,
        'release': values.release.strftime('%Y-%m-%d'),
        'description': values.description,
        'created_at': values.created_at,
        'updated_at': values.updated_at,
    }
    return render(request, 'shows_app/edit.html', context)

def update(request, id):
    errors = Shows.objects.validate(request.POST, 1)
    if errors:
        for key, value in errors.items():
            messages.error(request, {key: value})
        values = Shows.objects.display(id)
        context = {
            'id': values.id,
            'title': values.title,
            'network': values.network,
            'release': values.release.strftime('%Y-%m-%d'),
            'description': values.description,
            'created_at': values.created_at,
            'updated_at': values.updated_at,
        }
        return render(request, 'shows_app/edit.html', context)
    if request.method == "POST":
        id = Shows.objects.update(id, request.POST)
    return redirect(f'/shows/{id}')

def destroy(request, id):
    Shows.objects.destroy(id)
    return redirect('/shows')