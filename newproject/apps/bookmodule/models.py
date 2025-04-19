from django.db import models

class Book(models.Model):
    title = models.CharField(max_length = 50, null=True, blank=True)
    author = models.CharField(max_length = 50, null=True, blank=True)
    price = models.FloatField(default = 0.0)
    edition = models.SmallIntegerField(default = 1)

class Address(models.Model):
    city = models.CharField(max_length = 100, null=True, blank=True)
    
class Card(models.Model):
    card_number = models.IntegerField(default=0000)
    
class Department(models.Model):
    name = models.CharField(max_length = 100, null=True, blank=True)
   # students =models.ForeignKey(Student,on_delete=models.CASCADE)

class Course(models.Model):
    title = models.CharField(max_length = 100, null=True, blank=True)
    code = models.IntegerField(default=0000)

class Student(models.Model):
    name = models.CharField(max_length = 50, null=True, blank=True)
    address = models.ForeignKey(Address, on_delete=models.SET_NULL, null=True, blank=True)
    age = models.IntegerField(default = 1)

class Student2(models.Model):
    name = models.CharField(max_length = 50, null=True, blank=True)
    card =  models.OneToOneField(Card, on_delete=models.PROTECT , null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ManyToManyField(Course, related_name='students', null=True, blank=True)

class Student3(models.Model):
    name = models.CharField(max_length = 50, null=True, blank=True)
    card =  models.OneToOneField(Card, on_delete=models.PROTECT , null=True, blank=True)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    course = models.ManyToManyField(Course, related_name='student3', null=True, blank=True)