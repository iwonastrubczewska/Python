
from django.db import models

# Create your models here.
class Employer(models.Model):
    name = models.CharField(max_length=50)

class Employee(models.Model):
    name = models.CharField(max_length=50)
    phoneNumber = models.BigIntegerField

class Offer(models.Model):
    company = models.ForeignKey(Employer, models.CASCADE)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

class Form(models.Model):
    employee = models.ForeignKey(Employee, models.CASCADE)
    offer = models.ForeignKey(Offer, models.CASCADE)

class Question(models.Model):
    offer = models.ForeignKey(Offer, models.CASCADE)
    text = models.TextField

class Answer(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    form = models.ForeignKey(Form, models.CASCADE)
    text = models.TextField