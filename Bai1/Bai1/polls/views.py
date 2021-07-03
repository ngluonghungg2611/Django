from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def test(request):
    return HttpResponse("Chao moi nguoi lai minh Chao day")

def base(request):
    myname = "Sol Nguyen"
    context = {"name": myname}
    return render(request, "polls/base.html", context)
