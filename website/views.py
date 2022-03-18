from multiprocessing import Event
from turtle import setundobuffer
from django.shortcuts import render, redirect
from .models import Company, Member
from .forms import MemberForm, CompanyForm


def home(request):
    all_members = Member.objects.all
    return render(request, 'home.html', {'all': all_members})


def company_view(request):
    all_company = Company.objects.all
    return render(request, 'company_view.html', {'all': all_company})


def profiles(request):
    all_members = Member.objects.all().order_by('fname')
    return render(request, 'profiles.html', {'all': all_members})


def join(request):
    if request.method == "POST":
        form = MemberForm(request.POST or None)
        if form.is_valid():
            form.save()
        return render(request, 'join.html', {})

    else:
        return render(request, 'join.html', {})


def companyForm(request):
    if request.method == "POST":
        form1 = CompanyForm(request.POST or None)
        if form1.is_valid():
            form1.save()
        return render(request, 'companyForm.html', {})

    else:
        return render(request, 'companyForm.html', {})


def searchCompany(request):
    if request.method == "POST":
        searched = request.POST['searched']
        company = Company.objects.filter(companyName__contains=searched)
        return render(request, 'searchCompany.html', {'searched': searched, 'company': company})
    else:
        return render(request, 'searchCompany.html', {})


def studentList(request):
    all_members = Member.objects.all()
    return render(request, 'studentList.html', {'all': all_members})


def show_students(request, Member_id):
    showStudent = Member.objects.get(pk=Member_id)
    return render(request, 'show_students.html', {'all': showStudent})


def companyList(request):
    all_company = Company.objects.all()
    return render(request, 'companyList.html', {'all_company': all_company})


def show_company(request, Company_id):
    showcompany = Company.objects.get(pk=Company_id)
    return render(request, 'show_company.html', {'showcompany': showcompany})


def update_student(request, Member_id):
    updateStudent = Member.objects.get(pk=Member_id)
    form = MemberForm(request.POST or None, instance=updateStudent)
    if form.is_valid():
        form.save()
        return redirect('profiles')
    return render(request, 'updateStudent.html', {'all': updateStudent, 'form': form})


def update_company(request, Company_id):
    updateCompany = Company.objects.get(pk=Company_id)
    form = CompanyForm(request.POST or None, instance=updateCompany)
    if form.is_valid():
        form.save()
        return redirect('company_view')
    return render(request, 'updateCompany.html', {'all': updateCompany, 'form': form})

# Delete a student


def delete_student(request, Member_id):
    deleteStudent = Member.objects.get(pk=Member_id)
    deleteStudent.delete()
    return redirect('profiles')


def delete_company(request, Company_id):
    deleteCompany = Company.objects.get(pk=Company_id)
    deleteCompany.delete()
    return redirect('company_view')
