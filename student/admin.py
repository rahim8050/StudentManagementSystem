from django.contrib import admin

from student.models import Student

from student.models import Student
admin.site.site_header = 'Student Administration'
admin.site.site_title = 'Student Administration'
# Register your models here.
class StudentAdmin(admin.ModelAdmin):
    list_display = ('id', 'FirstName', 'LastName', 'Gender')
    list_filter = ('Gender',)
    list_per_page = 15
