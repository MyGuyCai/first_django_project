from django.shortcuts import render


def index(request):
    return render(request, 'graph_index.html')


def about_us(request):
    return render(request, "about_us.html")


def services(request):
    return render(request, "services.html")


def contact_us(request):
    return render(request, "contact_us.html")



