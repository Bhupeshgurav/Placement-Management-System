from socket import fromshare
from django import forms
from .models import Member, Company


class MemberForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['fname', 'lname', 'email', 'age', 'sex']


class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = ['srNo', 'companyName', 'jobTitle', 'jobLocation']
