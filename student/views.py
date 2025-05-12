from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request,'base.html')


def students(request):
    return render(request,'students.html')