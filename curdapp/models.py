from django.db import models

class StudentData(models.Model):
    first_name=models.CharField(max_length=50)
    last_name=models.CharField(max_length=50)
    course=models.CharField(max_length=50)
    fee=models.IntegerField()
    iname=models.CharField(max_length=50)
    mobile=models.BigIntegerField()
    email=models.EmailField(max_length=50)
    a1=models.IntegerField()
    a2=models.IntegerField()
    a3=models.IntegerField()
    a4=models.IntegerField()
    location=models.CharField(max_length=50)
