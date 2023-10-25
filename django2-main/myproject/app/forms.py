from django import forms

class UserForm(forms.Form):
    first_name = forms.CharField(
        max_length=100,
        min_length=5,
        label='Имя'
    )
    last_name = forms.CharField(
        max_length=100,
        min_length=5,
        label='Фамилия'
    )
    file = forms.FileField()

