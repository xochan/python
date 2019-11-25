from django.shortcuts import render, HttpResponse, redirect
from .models import *
def index(request):
    context = {
        'all_books':Book.objects.all(),
        'all_authors':Author.objects.all()
    }
    return render(request, 'books_authors_app/index.html',context )

def add_books(request):
    print(request.session)
    if request.method == 'POST':
        title = request.POST['title']
        desc = request.POST['desc']
        Book.objects.create(title=title, desc = desc)
        return redirect('/')

def bookinfor(request, num):
    print(request.method)
    
    book = Book.objects.get(id= num )
    
    context = {
    'title':book.title,
    'id': book.id,
    'authors': book.authors.all(),
    'all_authors': Author.objects.all()
    }
    print(context)
    return render(request, 'books_authors_app/books.html',context )

def updatebook(request):
    if request.method == 'POST':
        print(request.POST)
        id_author = request.POST['idauthor']
        id_book = request.POST['idbook']
        book = Book.objects.get(id=id_book)
        author = Author.objects.get(id=id_author)
        book.authors.add(author)
        book.save()
    return redirect('/books/'+ id_book)

def add_author(request):
    print(request.session)
    if request.method == 'POST':
        first = request.POST['first']
        last = request.POST['last']
        note = request.POST['note']
        Author.objects.create(first_name = first, last_name=last, notes=note)
        return redirect('/authors')
    else:
        context = {
        'all_books':Book.objects.all(),
        'all_authors':Author.objects.all()
        }
        return render(request, 'books_authors_app/authors.html',context)

def authorinfor(request, num):
    print(request.method)
    author = Author.objects.get(id= num )
    context = {
    'first':author.first_name,
    'last': author.last_name,
    'id': author.id,
    'note':author.notes,
    'books': author.books.all(),
    'all_books': Book.objects.all()
    }
    print(context)
    return render(request, 'books_authors_app/authors_info.html',context )

def updateauthor(request):
    if request.method == 'POST':
        print(request.POST)
        id_author = request.POST['idauthor']
        id_book = request.POST['idbook']
        book = Book.objects.get(id=id_book)
        author = Author.objects.get(id=id_author)
        book.authors.add(author)
        author.books.add(book)
        author.save()
    return redirect('/authors/'+ id_author)