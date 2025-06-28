from django import forms
from django.core.exceptions import ValidationError

from account.models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'age', 'phone', 'password', 'password2']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age is not None and age < 0:
            raise ValidationError("Yosh manfiy bo'lishi mumkin emas.")
        return age

    def clean_password2(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('password2')
        if password and password2 and password != password2:
            raise forms.ValidationError("Parollar mos emas!")
        return password2





    def save(self, commit=True):
        user = CustomUser(
            username=self.cleaned_data['username'],
            email=self.cleaned_data['email'],
            age=self.cleaned_data['age'],
            phone=self.cleaned_data['phone']
        )
        user.set_password(self.cleaned_data['password'])
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(label="Username", max_length=150, widget=forms.TextInput(attrs={'class': 'form-control'}))
    password = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={'class': 'form-control'}))




#
#
# class CustomUserCreationForm(forms.ModelForm):
#     password = forms.CharField(label='Password', widget=forms.PasswordInput)
#     password2 = forms.CharField(label='Password confirmation', widget=forms.PasswordInput)
#     class Meta:
#         model = CustomUser
#         fields = [
#             'username',
#             'email',
#             'age',
#             'phone',
#             'password',
#             'password2',
#
#         ]
#
#     def save(self, commit=True):
#         return CustomUser.objects.create_user(**self.cleaned_data)