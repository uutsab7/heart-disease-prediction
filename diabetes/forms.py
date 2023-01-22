from django import forms
from .models import Result, Contact, Result2


class ResultModelForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = "__all__"

class ContactModelForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class Result2ModelForm(forms.ModelForm):
    class Meta:
        model = Result2
        fields = "__all__"
        