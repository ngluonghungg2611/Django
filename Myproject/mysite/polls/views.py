from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    myname = "Sol Nguyen"
    lst = ["Điện thoại", "Laptop", "Bàn phím", "Tivi"]
    context = {"name": myname, "item": lst}
    return render(request,"polls/index.html", context)

