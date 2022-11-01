from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction
from authentication.models import VolundearUser

class RelawanSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = VolundearUser
        fields = {'username', 'full_name', 'email', 'password', 'password2', 'jenis_kelamin'}
    
    def __init__(self, *args, **kwargs):
        super(RelawanSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control register-relawan'
        self.fields['full_name'].widget.attrs['class'] = 'form-control register-relawan'
        self.fields['password'].widget.attrs['class'] = 'form-control register-relawan'
        self.fields['password2'].widget.attrs['class'] = 'form-control register-relawan'
        self.fields['jenis_kelamin'].widget.attrs['class'] = 'form-control register-relawan'

        for fieldname in ['username', 'full_name', 'password', 'password2', 'jenis_kelamin']:
            self.fields[fieldname].help_text = None
    
    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_relawan = True
        user.save()

        return user

class PJSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = VolundearUser
        fields = {'username', 'full_name', 'email', 'password', 'password2', 'jenis_kelamin'}

    def __init__(self, *args, **kwargs):
        super(PJSignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control register-relawan'
        self.fields['full_name'].widget.attrs['class'] = 'form-control register-relawan'
        self.fields['password'].widget.attrs['class'] = 'form-control register-relawan'
        self.fields['password2'].widget.attrs['class'] = 'form-control register-relawan'
        self.fields['jenis_kelamin'].widget.attrs['class'] = 'form-control register-relawan'

        for fieldname in ['username', 'full_name', 'password', 'password2', 'jenis_kelamin']:
            self.fields[fieldname].help_text = None


    def save(self):
        user = super().save(commit=False)
        user.is_PJ = True
        user.save()
        
        return user
