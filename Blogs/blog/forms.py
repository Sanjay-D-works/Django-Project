from django import forms

class ContactForm(forms.Form):
    name = forms.CharField(label='Name', max_length=100, required=True)
    email = forms.EmailField(label='Email',required=True)
    message = forms.CharField(label='Message',required=True)


class RegisterForm(forms.ModelForm):
    username = forms.CharField(label='Username', max_length=100, required=True)
    email = forms.CharField(label='Email', max_length=100, required=True)
    password = forms.CharField(label='Password', max_length=100, required=True)
    password_confirm = forms.CharField(label='Confirm Password', max_length=100, required=True)
