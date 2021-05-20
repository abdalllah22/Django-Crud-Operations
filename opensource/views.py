from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from opensource.models import Student, Track
from opensource.forms import StudentForm, TrackForm

# Create your views here.

def home(request):
    return HttpResponse("<h1> Hello  </h1>")

def getStudent(request,st_id):
    st = Student.objects.get(id = st_id)
    context = {'student':st}
    return render(request,'opensource/student_details.html',context)

def getAllStudent(request):
    all_students = Student.objects.all()
    context = {'students':all_students}
    return render(request, 'opensource/students.html' , context)

def newStudent(request):
    st_form = StudentForm()

    if request.method == 'POST':
        st_form = StudentForm(request.POST)
        if st_form.is_valid():
            st_form.save()
            return HttpResponseRedirect('/opensource/all')

    context = {'student_form':st_form}
    return render(request,'opensource/new_student.html',context)

def editStudent(request,st_id):
    st = Student.objects.get(id = st_id)

    st_form = StudentForm(instance = st)
    if request.method == 'POST':
        st_form = StudentForm(request.POST, instance=st)
        if st_form.is_valid():
            st_form.save()
            return HttpResponseRedirect('/opensource/all')

    context = {'student_form':st_form}
    return render(request, 'opensource/new_student.html', context)

def deleteStudent(request,st_id):
    st = Student.objects.get(id=st_id)
    st.delete()
    return HttpResponseRedirect('/opensource/all')