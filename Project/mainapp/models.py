

# Create your models here.
from django.db import models

# Create your models here.
class Employer(models.Model):
    id = models.IntegerField();
    name = models.CharField(max_length=50)

class User(models.Model):
    name = models.CharField(max_length=50)
    phone_no = models.BigIntegerField

class Offer(models.Model):
    company = models.ForeignKey(Employer, models.CASCADE)
    position = models.CharField(max_length=50)
    descryption = models.TextField

class Question(models.Model):  # sprawdzić czy potrzbene są pytania, czy każdy pracodawca ma sam wymyślaś swoej
    offer = models.ForeignKey (Offer, models.CASCADE)
    age = models.IntegerField
    education = models.TextField
    experience = models.TextField
    practice = models.TextField
    address = models.CharField(max_length=500)

class Form(models.Model):
    offer = models.ForeignKey (Offer, models.CASCADE)



class Answer(models.Model):
    question = models.ForeignKey(Question, models.CASCADE)





