from django.shortcuts import render, redirect
from .models import Note, Tag


def index(request):
    if request.method == 'POST':
        title = request.POST.get('titulo')
        content = request.POST.get('detalhes')
        note = Note()
        note.title = title
        note.content = content
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})

def update(request, id):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        id = request.POST.get('id')
        note = Note(id = id,title = title,content = content)
        note.save()
        return redirect('index')
    else:
        all_notes = Note.objects.all()
        return render(request, 'notes/index.html', {'notes': all_notes})
        
def delete(request, id):
    if request.method == 'POST':
        note = Note.objects.get(id=id)
        note.delete()
        return redirect('index')