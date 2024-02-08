from django.shortcuts import render
from .form import EmpForm
from .models import Employee
# Create your views here.

def Home(request):
    return render(request,'home.html')

def Add_Emp(request):
    if request.method == 'POST':
        f = EmpForm(request.POST,request.FILES)
        f.save()
        imgl = Employee.objects.all()
        context = {'form': f,'imgl':imgl}
        return render(request,'home.html', context)
    else:
        f = EmpForm
        context = {'form': f}
        return render(request,'addemp.html', context)
    

def Emp_List(request):
    f = Employee.objects.all()
    context = {'elist': f}
    return render(request,'emplist.html', context)
