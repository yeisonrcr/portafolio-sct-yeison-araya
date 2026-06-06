from django import forms
from .models.contact_message import ContactMessage


class ContactForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['name', 'email', 'company', 'subject', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Tu nombre completo'}),
            'email': forms.EmailInput(attrs={'placeholder': 'tu@empresa.com'}),
            'company': forms.TextInput(attrs={'placeholder': 'Empresa (opcional)'}),
            'subject': forms.TextInput(attrs={'placeholder': '¿En qué puedo ayudarte?'}),
            'message': forms.Textarea(attrs={
                'placeholder': 'Cuéntame sobre el proyecto o la necesidad de tu empresa...',
                'rows': 6
            }),
        }
