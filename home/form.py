from django import forms


class ContactForm(forms.Form):
    name = forms.CharField(label="Ihr Name", max_length=100)
    phone = forms.CharField(label="Telefonnummer", max_length=20, required=False)
    email = forms.EmailField(label="E-Mail Adresse", max_length=50)
    message = forms.CharField(
        label="Schreiben Sie eine Nachricht", widget=forms.Textarea
    )
