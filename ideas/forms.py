from django import forms
from django.contrib.auth.models import User

from ideas.models import Idea

class IdeaForm(forms.ModelForm):
    submitted_by = forms.ModelChoiceField(queryset=User.objects.all(), widget=forms.widgets.HiddenInput())
    class Meta:
        model = Idea
        exclude = ('date_modified', 'date_added')
