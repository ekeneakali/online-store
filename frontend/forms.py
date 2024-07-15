from django import forms

from.models import *

from django.core import validators

from django.contrib.auth.models import User

from django.contrib.auth.forms import (UserCreationForm, UserChangeForm)

from django.utils.translation import gettext as _

from django.contrib.auth.forms import SetPasswordForm

from django.contrib.auth.forms import PasswordResetForm



class Register(UserCreationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter username'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter first name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'enter last name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control', 'placeholder':'enter your email'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter password1'}))
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control', 'placeholder':'enter password2'}))
    botfield = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])

    

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', 'password1', 'password2']


    def save(self, commit=True):
        user = super().save(commit=False)
        user.username = self.cleaned_data['username']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']
        user.email = self.cleaned_data['email']
        user.password1 = self.cleaned_data['password1']
        user.password2 = self.cleaned_data['password2']

        if commit:
            user.save()
        return user

class EditProfile(UserChangeForm):

    class Meta():
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

CHOICE = [
    ('select1', 'seller'),
    ('select3', 'buyer'),
    ('select3', 'hybrid'),

]


class Info(forms.Form):
    first_name = forms.CharField()
    last_name = forms.CharField()
    email = forms.EmailField()
    favorite = forms.MultipleChoiceField(label='select account', widget=forms.RadioSelect, choices=CHOICE,)
    date = forms.IntegerField()
    notify = forms.BooleanField(label='notify me when needed')
    botfield = forms.CharField(widget=forms.HiddenInput, required=False, validators=[validators.MaxLengthValidator(0)])


class ContactForm(forms.ModelForm):

    class Meta():
        model = Contact
        fields = '__all__'

class NewsLetterForm(forms.ModelForm):

    class Meta():
        model = Contact
        fields = '__all__'



class SetPasswordForm(SetPasswordForm):
    class Meta:
        model = User()
        fields = ['new_password1', 'new_password2']


class PasswordResetForm(PasswordResetForm):
    def __init__(self, *args, **kwargs):
        super(PasswordResetForm, self).__init__(*args, **kwargs)

    # captcha = ReCaptchaField(widget=ReCaptchaV2Checkbox())


class ProductForm(forms.ModelForm):

    class Meta():
        model = Product
        fields = '__all__'
        exclude = ['likes', 'favourite', 'user']

class ProfileForm(forms.ModelForm):

    class Meta():
        model = Profile
        fields = '__all__'

class VideoForm(forms.ModelForm):

    class Meta():
        model = Video
        fields = '__all__'
        exclude = ['user']

