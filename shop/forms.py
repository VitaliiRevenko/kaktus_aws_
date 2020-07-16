from django import forms

class SendForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)
    your_tel_number = forms.CharField(label='Your tel.number', max_length=20)
    your_email = forms.EmailField()
    send_text = forms.CharField(max_length=500)
