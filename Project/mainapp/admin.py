# Register your models here.
from django.contrib import admin
from .models import (Company, User, Offer, Form, Question, Answer)

admin.site.register(Company)
admin.site.register(User)
admin.site.register(Offer)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Answer)
