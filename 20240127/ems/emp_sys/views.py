from django.shortcuts import render,HttpResponse

from .models import Company, Employee

# Create your views here.

def home(request):
    return render(request, 'home.html')

def all_emp(request):
    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'employees.html', context)

def all_comp(request):
    comps = Company.objects.all()
    context = {
        'comps' : comps
    }
    return render(request, 'company.html', context)

def comp(request,id):
    comp_emp = Company.objects.get(id = id)
    emps = Employee.objects.filter(company = comp_emp)
    context = {
        'emps' : emps
    }
    return render(request, 'employees.html', context)

def del_comp(request,id):
    comp = Company.objects.get(id = id)
    comp.delete()

    comps = Company.objects.all()
    context = {
        'comps' : comps
    }
    return render(request, 'company.html', context)


def del_emp(request,id):
    emp = Employee.objects.get(id = id)
    emp.delete()

    emps = Employee.objects.all()
    context = {
        'emps' : emps
    }
    return render(request, 'employees.html', context)

def add_emp(request):
    try:
        if request.method == 'GET':
            comps = Company.objects.all()
            context = {
                'comps' : comps
            }
            return render(request, 'add_emp.html', context)
        else:
                firstname = request.POST['firstname']
                lastname = request.POST['lastname']
                post = request.POST['post']
                company = request.POST['company']

                comps = Company.objects.get(name = company)

                emp = Employee(firstname = firstname,lastname = lastname, post = post, company = comps)
                emp.save()


                emps = Employee.objects.all()
                context = {
                'emps' : emps
            }
                return render(request, 'employees.html', context)
    except Exception as e:
        print(e)
        comps = Company.objects.all()
        context = {
                'comps' : comps
            }
        return render(request, 'add_emp.html', context)

def add_comp(request):
    try:
        if request.method == 'GET':
            return render(request, 'add_comp.html')
        else:
            name = request.POST['name']
            type = request.POST['type']
            location = request.POST['location']

            comp = Company(name = name, type = type, location = location)
            comp.save()


            comps = Company.objects.all()
            context = {
                'comps' : comps
            }
            return render(request, 'company.html', context)
    except Exception as e:
        comps = Company.objects.all()
        context = {
                'comps' : comps
            }
        return render(request, 'add_comp.html')
