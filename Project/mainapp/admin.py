
from django.contrib import admin
from .models import (Employee, Employer, Offer, Form, Question, Answer)

admin.site.register(Employee)
admin.site.register(Employer)
admin.site.register(Offer)
admin.site.register(Form)
admin.site.register(Question)
admin.site.register(Answer)