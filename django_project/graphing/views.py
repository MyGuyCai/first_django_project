from django.conf import settings
from django.shortcuts import render
from django.core.files.storage import FileSystemStorage


def index(request):
    context = {}
    if request.method == 'POST':
        context = {}
        uploaded_file = request.FILES['document']
        print(uploaded_file.name, uploaded_file.size)
        fs = FileSystemStorage()
        name = fs.save(uploaded_file.name, uploaded_file)
        context['url'] = fs.url(name)

    return render(request, 'graph_index.html', context)
