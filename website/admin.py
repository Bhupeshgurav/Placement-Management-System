from django.contrib import admin

from .models import Company, Member
admin.site.register(Member)
admin.site.register(Company)
