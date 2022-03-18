from django.db import models


class Member(models.Model):
    fname = models.CharField(max_length=50)
    lname = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    age = models.IntegerField()
    sex = models.CharField(max_length=50)

    def __str__(self):
        return self.fname + ' ' + self.lname


class Company(models.Model):
    srNo = models.IntegerField()
    companyName = models.CharField(max_length=50)
    jobTitle = models.CharField(max_length=100)
    jobLocation = models.CharField(max_length=100)

    def __str__(self):
        return self.companyName
