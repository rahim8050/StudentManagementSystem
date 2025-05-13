from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render

from student.models import Student


# Create your views here.
def studentlist(request):
        students = Student.objects.all().order_by('-created_at')
        return render(request, 'students.html', {'students': students})


def students(request):
    return render(request,'students.html')
