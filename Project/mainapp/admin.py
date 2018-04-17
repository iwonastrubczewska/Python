# Register your models here.
from django.contrib import admin
from .models import (Employer, User, Offer)

admin.site.register(Employer)
admin.site.register(User)
admin.site.register(Offer)
