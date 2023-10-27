from django.shortcuts import render

def home(request):
    return render(request, "home.html")


def record(request):
    return render(request, "record.html")