from django.db import models

# Create your models here.


class StudentInfo(models.Model):
    studentid = models.IntegerField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    studentmajor = models.CharField(max_length=100)
    studentyear = models.CharField(max_length=100)
    gpa = models.DecimalField(max_digits=2, decimal_places=1)

class CourseInfo(models.Model):
    courseid = models.IntegerField(primary_key=True)
    coursetitle = models.CharField(max_length=100)
    coursename = models.CharField(max_length=100)
    coursesection = models.IntegerField()
    coursedepartment = models.CharField(max_length=100)
    instructor = models.CharField(max_length=100)

class EnrollmentInfo(models.Model):
    enrollmentid = models.IntegerField(primary_key=True)
    studentid = models.ForeignKey(StudentInfo, default=1, verbose_name="student", on_delete=models.CASCADE)
    courseid = models.ForeignKey(CourseInfo, default=1, verbose_name="course", on_delete=models.CASCADE)
    
# migrate, makemigrations