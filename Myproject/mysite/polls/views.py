from django.shortcuts import render
from django.http import HttpResponse
def Bai1(request):
    return render(request, 'polls/Bai1.html')
def Bai2(request):
    return render(request, 'polls/Bai2.html')
def Bai3(request):
    return render(request, 'polls/Bai3.html')