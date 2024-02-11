# from .crawl_book import crawl
from django.shortcuts import render

from .forms import BookSearchForm
from .models import Book
from .utils import crawl  # Import  crawl function

# Create your views here.
base_url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&q={book_name}&search_type=book'

def book_list(request):
    books = Book.objects.all()
    return render(request, 'book_list.html', {'books': books})


def search_books(request):
    if request.method == 'POST':
        form = BookSearchForm(request.POST)
        if form.is_valid():
            book_name = form.cleaned_data['book_name']

            URL = base_url.format(book_name=request.POST['book_name'])  # Corrected line

            # Call your crawl function with the entered book name
            crawl(URL)
            books = Book.objects.all()

            return render(request, 'book_list.html', {'books': books})
    else:
        form = BookSearchForm()
    return render(request, 'search_books.html', {'form': form})
