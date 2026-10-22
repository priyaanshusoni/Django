from django.shortcuts import render
from django.http import HttpResponse
from .models import Book, BookInstance, Author, Genre
from django.views import generic

# Create your views here.


def index(request):

    num_books = Book.objects.all().count()

    num_instances = BookInstance.objects.all().count()

    # Available books (status = 'a')
    num_instances_available = BookInstance.objects.filter(status="a").count()

    # The 'all()' is implied by default.
    num_authors = Author.objects.count()

    genre = Genre.objects.count()

    context = {
        "num_books": num_books,
        "num_instances": num_instances,
        "num_instances_available": num_instances_available,
        "num_authors": num_authors,
        "genre": genre,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, "catalog/index.html", context=context)


class BookListView(generic.ListView):
    model = Book
    context_object_name = "book_list"
    paginate_by = 10

    """
      template_name = 'books/my_arbitrary_template_name_list.html'  # Specify your own template name/location
    
    """


class BookDetailView(generic.DetailView):
    model = Book
