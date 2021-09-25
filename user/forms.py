from django import forms
from django.db.models import fields
from . import models

class FormMixin(forms.ModelForm):
    ...


class UserDeatilForm(forms.ModelForm):
    class Meta:
        model = models.UserDetails
        fields = "__all__"
    
    
    def clean(self):
        breakpoint()
        cleaned_data = super().clean()
        super().clean()['user']


class SkillForm(forms.ModelForm):
    class Meta:
        model = models.Skills
        fields = "__all__"