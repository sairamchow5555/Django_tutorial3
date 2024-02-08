from django.shortcuts import render
from testapp.models import Book
from django.views.generic import ListView,DetailView,CreateView,UpdateView,DeleteView
# Create your views here.
#def list_view(request):
#    books_list = Book.objects.all()
#    return render(request,'testapp/books.html',{'books_list':books_list})

class BookListView(ListView):
    model = Book
    #default template file:book_list.html
    #default context object name:book_list
    #template_name = 'testapp/book.html'
    #context_object_name = 'books'

class BookListView2(ListView):
    model = Book
    template_name = 'testapp/book.html'
    context_object_name = 'books'

class BookDetailView(DetailView):
    model = Book
    #default template file:book_detail.html
    #default context object name:book or object

class BookCreateView(CreateView):
    model = Book
    fields = '__all__'

class BookUpdateView(UpdateView):
    model = Book
    fields = ['title','author','pages','price'] #or ['__all__']
    #the default template is: book_form.html

from django.urls import reverse_lazy
class BookDeleteView(DeleteView):
    model = Book
    success_url = reverse_lazy('listbooks')
