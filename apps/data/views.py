from django.shortcuts import render

# Create your views here.
def bar(request):
    return render(request,'render.html')