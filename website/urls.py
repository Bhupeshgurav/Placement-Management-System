from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('company_view/', views.company_view, name="company_view"),
    path('profiles/', views.profiles, name="profiles"),
    path('join/', views.join, name="join"),
    path('companyForm/', views.companyForm, name="companyForm"),
    path('searchCompany/', views.searchCompany, name="searchCompany"),
    path('studentList/', views.studentList, name="studentList"),
    path('show_students/<Member_id>',
         views.show_students, name="show-students"),
    path('companyList/', views.companyList, name="companyList"),
    path('show_company/<Company_id>',
         views.show_company, name="show-company"),
    path('update_student/<Member_id>',
         views.update_student, name="update-students"),
    path('delete_student/<Member_id>',
         views.delete_student, name='delete-students'),
    path('update_company/<Company_id>',
         views.update_company, name="updateCompany"),
    path('delete_company/<Company_id>',
         views.delete_company, name='delete-company'),
]
