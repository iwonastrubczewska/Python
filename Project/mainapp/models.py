
from django.db import models

class User(models.Model):
    name = models.CharField(max_length=50)
    isEmployer = models.BooleanField(default=False)

class Company(models.Model):
    name = models.CharField(max_length=50)

class Offer(models.Model):
    company = models.ForeignKey(Company, models.CASCADE)
    position = models.CharField(max_length=50)
    description = models.TextField
    startDate = models.DateTimeField
    endDate = models.DateTimeField

class Form(models.Model):
    offer = models.ForeignKey(Offer, models.CASCADE)

class Question(models.Model):
    offer = models.ForeignKey(Offer, models.CASCADE)
    text = models.TextField

class Answer(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)
    form = models.ForeignKey(Form, models.CASCADE)
    text = models.TextField



