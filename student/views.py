from urllib import request

from django.contrib import messages
from django.core.paginator import EmptyPage, Paginator
from django.shortcuts import render, redirect, get_object_or_404

from student.forms import StudentForm
from student.models import Student


# Create your views here.
def studentlist(request):
    students = Student.objects.all().order_by('-created_at')
    return render(request, 'students.html', {'students': students})


# views.py

def DeleteStudent(request, student_id):
    student = Student.objects.get(id=student_id)  # select * from Warden table  where id=??
    student.delete()  # delete from Warden where id = ??
    # messages.info(request, f"Warden {warden.FirstName} was deleted")
    return redirect('students')


# def UpdateStudent(request, student_id):
#     student = get_object_or_404(Student, StudentID=student_id)
#     # Your update logic here
def students(request):
    return render(request, 'students.html')


def UpdateStudent(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    if request.method == 'POST':
        form = StudentForm(request.POST,request.FILES, instance=student)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your student has been updated.')
            return redirect('students')
    else:
        form = StudentForm(instance=student)
    return render(request, 'StudentUpdateForm.html', {"form": form})