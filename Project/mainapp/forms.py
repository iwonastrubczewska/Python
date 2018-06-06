from django import forms

from .models import Offer, Employee


class OfferForm(forms.ModelForm):
    class Meta:
        model = Offer
        fields = ('position', 'description', 'startDate', 'endDate')


class NewUserForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name',)

class UserForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name',)

#TO TRZEBA DOPISAĆ ( NIE WIEM, JAKIŚ MODEL ? )
class ContactForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = ('name',)
