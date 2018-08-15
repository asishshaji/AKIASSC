from django import forms
from .models import EnquiryModel


class EnquiryForm(forms.ModelForm):
    class Meta:
        model = EnquiryModel
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'id': 'con_name','name':'con_name','class':'required', 'placeholder': 'Your Name*'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Your Email*'}),
            'message': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'Message*'})
        }
