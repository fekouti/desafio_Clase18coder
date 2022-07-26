from multiprocessing import context
from django.http import HttpResponse
from django.shortcuts import render

def desafio(request):
    return render(request, "index.html", context={})


