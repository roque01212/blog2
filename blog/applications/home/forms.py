from django import forms
from .models import Suscribers, Contact


class SuscribersForm(forms.ModelForm):
    """Form definition for Sucribers."""

    class Meta:
        """Meta definition for Sucribersform."""
        model = Suscribers
        fields = ('email',)
        widgets = {
            'email': forms.EmailInput(
                attrs={
                    'placeholder':'Correo electronico'
                }
            )
        }

    
class ContactForm(forms.ModelForm):
    """Form definition for Sucribers."""

    class Meta:
        """Meta definition for Sucribersform."""
        model = Contact
        fields = (
            'full_name',
            'email',
            'message',
        )

    

