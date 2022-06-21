from django.core.paginator import InvalidPage, EmptyPage, Paginator
from django.shortcuts import render, get_object_or_404
# Create your views here.
from .models import Author,Books


def allbook(request, c_slug=None):
    c_page = None
    books = None
    if c_slug != None:
        c_page = get_object_or_404(Author,slug=c_slug)
        books = Books.objects.all().filter(author=c_page)
    else:
        books = Books.objects.all().filter()
        paginator = Paginator(books, 6)
    try:
        page = int(request.GET.get('page','1'))
    except:
        page = 1
    try:
        books = paginator.page(page)
    except(EmptyPage, InvalidPage):
        books = paginator.page(paginator.num_pages)

    return render(request,'home.html',{'author':c_page,'books': books})

