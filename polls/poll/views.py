from django.shortcuts import render,HttpResponse

# Create your views here.
def HomeView(request):
    return HttpResponse("Hello, world. 91dacc0f is the polls index.")
