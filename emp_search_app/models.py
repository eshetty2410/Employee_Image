from django.db import models

# Create your models here.

class Employee(models.Model):
    empid = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    age = models.IntegerField()
    address = models.CharField(max_length=300)
    photo = models.ImageField(upload_to='photos',null=True,blank=True,default='')


    class Meta:
        db_table = 'Emp'
