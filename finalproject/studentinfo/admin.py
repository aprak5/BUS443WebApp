from django.contrib import admin
from studentinfo.models import StudentInfo, CourseInfo, EnrollmentInfo

# Register your models here.

admin.site.register(StudentInfo)
admin.site.register(CourseInfo)
admin.site.register(EnrollmentInfo)
