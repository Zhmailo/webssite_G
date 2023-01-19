from django import forms

from apps.user.models import User


class LoginForm(forms.Form):
    username = forms.CharField(required=True)
    password = forms.CharField(required=True, max_length=64, widget=forms.PasswordInput)


class RegisterForm(forms.ModelForm):
    password_confirm = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'image', 'first_name', 'last_name', 'email', 'phone',
                  'about', 'password', 'password_confirm']

    def clean_email(self):
        cleaned_data = self.cleaned_data
        user = User.objects.filter(email=cleaned_data['email'])
        if user:
            raise forms.ValidationError('Користувач з таким E-mail вже існує')
        return cleaned_data['email']

    def clean_password_confirm(self):
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password_confirm']:
            raise forms.ValidationError('Паролі не співпадають')
        return cleaned_data['password_confirm']
