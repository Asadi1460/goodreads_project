from django import forms

class BookSearchForm(forms.Form):
    book_name = forms.CharField(label='Enter a Book Name')
