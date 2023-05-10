from django import forms
from ..models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].widget.attrs.update({
            'class': 'form-control py-2',
            'type': "text",
            'required': "required",
        })
        self.fields['email'].widget.attrs.update({
            'class': 'form-control py-2',
            'type': "email",
            'required': "required",
        })
        self.fields['body'].widget.attrs.update({
            'class': 'form-control py-2',
            'required': "required",
        })

