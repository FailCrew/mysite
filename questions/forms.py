from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from users.models import CustomUser

class ChallengerChoice(forms.Form):
    challenger = forms.ModelChoiceField(queryset=CustomUser.objects.all())

class Answer(forms.Form):
    answer = forms.CharField(min_length=1, max_length=30)
    