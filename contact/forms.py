from django.forms import ModelForm,EmailInput,Textarea
from .models import Contact

class ContactForm(ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            "email":EmailInput(attrs={
                'required':True,
                'class':'form-control',
                'placeholder':"Email"
            }),
            'message':Textarea(attrs={
                'required':True,
                'class':'form-control',
                'placeholder':'message'
            })
        }