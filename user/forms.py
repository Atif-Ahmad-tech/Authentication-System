from allauth.account.forms import SignupForm
from django import forms

class CustomSignupForm(SignupForm):
    first_name = forms.CharField(max_length=100, required=True)
    last_name = forms.CharField(max_length=100, required=True)
    def save(self, request):
        user = super().save(request)
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.save()
        return user

