from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from .models import Review


class RegistrationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)


class UserEditForm(forms.ModelForm):
    username = forms.CharField(max_length=30,required=False)
    email = forms.EmailField(required=False)
    old_password = forms.CharField(widget=forms.PasswordInput,required=False)
    new_password1 = forms.CharField(widget=forms.PasswordInput,required=False)
    new_password2 = forms.CharField(widget=forms.PasswordInput,required=False)

    class Meta:
        model = User
        fields = ('username', 'email', 'old_password', 'new_password1','new_password2')

    def clean_username(self):
        username = self.cleaned_data['username']
        if User.objects.filter(username=username).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Username is already taken.')
        return username

    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(email=email).exclude(pk=self.instance.pk).exists():
            raise ValidationError('Email is already taken.')
        return email

    def clean_old_password(self):
        old_password = self.cleaned_data['old_password']
        if not self.instance.check_password(old_password):
            raise ValidationError('Old password is incorrect.')
        return old_password

    def clean_new_password(self):
        new_password1 = self.cleaned_data['new_password1']
        new_password2 = self.cleaned_data['new_password2']
        if new_password1 and new_password2 and new_password1 != new_password2:
            raise ValidationError('New passwords do not match.')
        return new_password2

    def save(self, commit=True):
        user = super().save(commit=False)
        if self.cleaned_data['username']:
            user.username = self.cleaned_data['username']
        if self.cleaned_data['email']:
            user.email = self.cleaned_data['email']
        if self.cleaned_data['new_password1']:
            user.set_password(self.cleaned_data['new_password1'])
        if commit:
            user.save()
        return user


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ('text',)
        widgets = {
            "text": forms.Textarea(attrs={"class": "form-control border"})
        }
