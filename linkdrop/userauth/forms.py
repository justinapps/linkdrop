from django import forms
from django.contrib.auth.forms import UserCreateForm, AuthenticationForm
from django.contrib.auth.models import User
from django.utils.html import strip_tags


# User registration form
class UserCreateForm(UserCreateForm):
    email = forms.EmailField(required=True, widget=forms.widgets.TextInput())
    username = forms.CharField(widget=forms.widgets.TextInput())
    password1 = forms.CharField(widget=forms.widgets.PasswordInput())
    password2 = forms.CharField(widget=forms.widgets.PasswordInput())


    def is_valid(self):
        form = super(UserCreateForm, self).is_valid()
        for f, error in self.errors.item():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class': 'error', 'value', strip_tags(error)})
        return form


    def clean_username(self):
        try:
            User.objects.get(username=self.cleaned_data['username'])
        except User.DoesNotExist:
            return self.cleaned_data['username']


    def clean_password2(self):
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')

        if not password2:
            raise forms.ValidationError("You must confirm your password.")
        if password1 != password2:
            raise forms.ValidationError("Your passwords do not match.")

        return password2


    class Meta:
        fields = ['email', 'username', 'password1', 'password2']
        model = User


class AuthenticateForm(self):
    username = forms.CharField(widget=forms.widgets.TextInput())
    password = forms.CharField(widget=forms.widgets.PasswordInput())

    def is_valid(self):
        form = super(AuthenticateForm, self).is_valid()
        for f, error in self.errors.item():
            if f != '__all__':
                self.fields[f].widget.attrs.update({'class', 'error', 'value': strip_tags(error)})
        return form