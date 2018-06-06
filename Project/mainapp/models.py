from django.db import models

# Create your models here.
from django.urls import reverse


class Employer(models.Model):
    name = models.TextField()
    def __str__(self):
        return self.name[:50]

class Employee(models.Model):
    name = models.CharField(max_length=50)
    phoneNumber = models.BigIntegerField
    def __str__(self):
        return self.name[:50]

class Offer(models.Model):
    company = models.ForeignKey(Employer, models.CASCADE)
    position = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    startDate = models.DateTimeField()
    endDate = models.DateTimeField()

    def get_url(self):
        return reverse('offer',args=[str(self.id)])

    def __str__(self):
        return "%s: %s " %(self.company.name, self.position)

class Form(models.Model):
    employee = models.ForeignKey(Employee, models.CASCADE)
    offer = models.ForeignKey(Offer, models.CASCADE)
    def __str__(self):
        return "%s (%s) " %(self.offer, self.employee)

class Question(models.Model):
    offer = models.ForeignKey(Offer, models.CASCADE)
    text = models.TextField
    def __str__(self):
        return "%s: %s " %(self.offer, self.text[:50])

class Answer(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    form = models.ForeignKey(Form, models.CASCADE)
    text = models.TextField
    def __str__(self):
        return self.text[:50]