from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from django.db.models import Avg, Count
from studentinfo.models import StudentInfo, CourseInfo, EnrollmentInfo


# Create your views here.
@login_required
def home(request):
    context = {'averageGPA': '{:.2f}'.format(StudentInfo.objects.aggregate(Avg("gpa"))['gpa__avg']), 'countStudents': StudentInfo.objects.aggregate(Count("studentid"))['studentid__count'], 'countCourses':CourseInfo.objects.aggregate(Count("courseid"))['courseid__count'], 'countFreshmen': StudentInfo.objects.filter(studentyear="Freshman").aggregate(Count("studentid"))['studentid__count'], 'countSophomores': StudentInfo.objects.filter(studentyear="Sophomore").aggregate(Count("studentid"))['studentid__count'], 'countJuniors': StudentInfo.objects.filter(studentyear="Junior").aggregate(Count("studentid"))['studentid__count'], 'countSeniors': StudentInfo.objects.filter(studentyear="Senior").aggregate(Count("studentid"))['studentid__count']}
    return render(request, 'studentinfo/home.html', context)
@login_required
def getStudentInfo(request):
    studentdata = StudentInfo.objects.all()
    paginator = Paginator(studentdata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data': pagedata}
    return render(request, 'studentinfo/studentinfo.html', context)
@login_required
def getCourseInfo(request):
    coursedata = CourseInfo.objects.all()
    paginator = Paginator(coursedata, 10)
    page = request.GET.get('page')
    pagedata = paginator.get_page(page)
    context = {'data': pagedata}
    return render(request, 'studentinfo/courseinfo.html', context)
@login_required
def enrollment(request):
    students = StudentInfo.objects.distinct()
    context = {'students': students}
    if request.method == "POST":
        return HttpResponseRedirect('http://127.0.0.1:8000/enrollment_page/' + request.POST['student.studentid'] + '/')
    else:
        return render(request, 'studentinfo/enrollment.html', context)
@login_required
def enrollment_page(request, studentid):
    context = {'studentInfo': StudentInfo.objects.get(studentid=studentid), 'courseInfo': CourseInfo.objects.all(), 'enrollmentInfo': None}
    try:
        context['enrollmentInfo'] = EnrollmentInfo.objects.filter(studentid_id=studentid)
    except:
        context['enrollmentInfo'] = None
    if request.method == "POST":
        try:
            cond1 = EnrollmentInfo.objects.get(studentid_id = studentid, courseid_id = request.POST['course.courseid'])
        except:    
            cond1 = None
        try:
            cond2 = len(EnrollmentInfo.objects.filter(studentid_id = studentid))
        except:    
            cond2 = 0
        try:
            newId = EnrollmentInfo.objects.last().enrollmentid + 1
        except:
            newId = 1        
        if cond1 == None and cond2 < 3:
            EnrollmentInfo.objects.create(enrollmentid = newId, studentid_id = studentid, courseid_id = request.POST['course.courseid'])
            return HttpResponseRedirect('http://127.0.0.1:8000/enrollment_page/' + str(studentid) + '/')
        else:
            return HttpResponseRedirect('http://127.0.0.1:8000/enrollment_page/' + str(studentid) + '/')        
    return render(request, 'studentinfo/enrollment_page.html', context)
