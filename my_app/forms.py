

from django import forms
from . models import cm
class ContactForm(forms.Form):
     model=cm

     fields = ['name','email','subject','message']