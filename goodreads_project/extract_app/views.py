# Import necessary modules
# from .crawl_book import crawl  # Assuming this line is commented out intentionally
from django.shortcuts import render

from .forms import BookSearchForm
from .models import Book
from .utils import crawl  # Import  crawl function

# Create your views here.
# Define the base URL for the Goodreads search
# base_url = 'https://www.goodreads.com/search?utf8=%E2%9C%93&q={book_name}&search_type=book'
base_url = (
    'https://www.goodreads.com/search?page={page_no}&q={'
    'book_name}&qid=11EtNnSlHA&search_type=books&tab=books&utf8=%E2%9C%93'
)


# View function for listing all books
def book_list(request):
    # Retrieve all books from the database
    books = Book.objects.all()
    # Render the template with the list of books
    return render(request, 'book_list.html', {'books': books})


# View function for searching books
def search_books(request):
    if request.method == 'POST':
        # If the request method is POST, process the form data
        form = BookSearchForm(request.POST)
        if form.is_valid():
            # If the form data is valid, extract the book name from the form
            # and search for it on Goodreads
            for page_number in range(1, 6):
                url = base_url.format(
                    page_no=page_number, book_name=request.POST['book_name']
                )
                # Call the crawl function to extract book data
                crawl(url)
            # Retrieve all books from the database
            books = Book.objects.all()
            # Render the template with the list of books
            return render(request, 'book_list.html', {'books': books})
    else:
        # If the request method is not POST, display the empty search form
        form = BookSearchForm()
    # Render the search form template with the form
    return render(request, 'search_books.html', {'form': form})
