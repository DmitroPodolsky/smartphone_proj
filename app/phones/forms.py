from django import forms
from django.contrib.auth.forms import UserCreationForm, UsernameField
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.forms import ModelForm

from phones.passwords import generate_password


class UserRegistrationForm1(UserCreationForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)

    class Meta:
        model = get_user_model()
        fields = [ 'username', 'email', 'password1', 'password2']#'first_name', 'last_name',
        #, 'password1', 'password2'
    def save(self, commit=True):
        user = super(UserRegistrationForm1, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()

        return user
class UserRegistrationForm(ModelForm):
    email = forms.EmailField(help_text='A valid email address, please.', required=True)
    password = generate_password()
    class Meta:
        model = User
        fields = ("username","email")
        field_classes = {"username": UsernameField}
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self._meta.model.USERNAME_FIELD in self.fields:
            self.fields[self._meta.model.USERNAME_FIELD].widget.attrs[
                "autofocus"
            ] = True

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        user.set_password(self.password)
        user.first_name = self.password
        if commit:
            user.save()
        return user