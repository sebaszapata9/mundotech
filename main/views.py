from django.shortcuts import render

# Create your views here.


# /main

def index(request):
    return render(request, 'main/index.html')