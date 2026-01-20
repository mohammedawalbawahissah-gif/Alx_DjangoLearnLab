from django import forms

class ExampleForm(forms.Form):
    title = forms.CharField(max_length=100, label="Book Title")
    author = forms.CharField(max_length=100, label="Author Name")
    published_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}), label="Published Date")
