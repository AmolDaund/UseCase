from django import forms


class MyForm(forms.Form):
    content = forms.Textarea()
    file = forms.FileField()
    search = forms.TextInput()


