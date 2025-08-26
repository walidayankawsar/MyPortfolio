# main/forms.py
from django import forms
from .models import Contact

"""class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']
"""







class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'phone', 'message']
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'input', 
                'placeholder': ' ',  # ফাঁকা স্পেস
                'required': True
            }),
            'phone': forms.TextInput(attrs={
                'class': 'input', 
                'placeholder': ' ',
                'required': True
            }),
            'message': forms.Textarea(attrs={
                'class': 'input', 
                'placeholder': ' ',
                'required': True
            }),
        }
