from django import forms

class UserForm(forms.Form):
    WC_WORDS = forms.IntegerField(
        max_value=1000,
        min_value=888,
        label='количество слов на картинке'
    )
    file = forms.FileField()

