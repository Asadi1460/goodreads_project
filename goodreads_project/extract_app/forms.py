from django import forms


class BookSearchForm(forms.Form):
    book_name = forms.CharField(label='Enter a Book Name')
    # num_pages = forms.IntegerField(label='Number of Pages', required=False)
