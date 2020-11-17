from django.http import HttpResponse
from django.shortcuts import render
def hi(request):
    msg="<h1>hello sreenath</h1>"
    return HttpResponse(msg)
def design(request):
    return render(request,'design.html')

