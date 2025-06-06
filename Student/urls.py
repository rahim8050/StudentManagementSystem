"""
URL configuration for Student project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include

from student import views

urlpatterns = [
    path('', views.studentlist, name='students'),
    path('Students/delete/<int:student_id>', views.DeleteStudent, name='DeleteStudent'),
    path('Students/update/<int:student_id>',views.UpdateStudent,name='UpdateStudent'),
    path('students/', views.students, name='students'),
    path('users/', include("users.urls")),
    path('admin/', admin.site.urls),
]
