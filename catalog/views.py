from typing import Any
from django.shortcuts import render

from .models import Author, Genre, Book, BookInstance, Language

# Create your views here.
def index(request):

    num_books = Book.objects.all().count()
    num_copied = BookInstance.objects.all().count()
    num_genre = Genre.objects.all().count()
    num_authors = Author.objects.all().count()
    num_language = Language.objects.all().count()

    #Create a variable call num_visit to count how many time we visited 'index.html'
    num_visits = request.session.get('num_visits', 0)
    request.session['num_visits'] = num_visits + 1

    #Context Data must be Diction
    context_book = {
        'num_books': num_books,
        'num_copied': num_copied,
        'num_genre': num_genre,
        'num_authors': num_authors,
        'num_language': num_language,

        # Adding Session's Cookies to Display in 'index.html'
        'num_visits': num_visits
    }

    return render(request, 'index.html', context=context_book)

from django.views import generic

class BookListView(generic.ListView):
    model = Book

    def get_context_data(self, **kwargs):
        context_book_list = super().get_context_data(**kwargs)

        num_visit_book_list = self.request.session.get('num_visit_book_list', 0)
        self.request.session['num_visit_book_list'] = num_visit_book_list + 1

        context_book_list = {
            "num_visit_book_list": num_visit_book_list
        }
        return context_book_list
    
class BookDetailView(generic.DetailView):
    model = Book