from django.shortcuts import render, redirect
from django.http import HttpResponse

from used_book.models import Book

# Create your views here.
def view(request):
    context = {}
    if request.method == 'GET':
        books = Book.objects.all()
        context = {'books':books}
        return render(request, 'used_book_view.html', context)
    elif request.method == 'POST':
        pk = request.POST.get('pk')
        try:
            book = Book.objects.get(pk=pk)
            book.delete()
            books = Book.objects.all()
            context = {'books':books}
        except Exception as e:
            context = {'error':e}
        return render(request, 'used_book_view.html', context)


def post(request):
    if request.method == 'GET':
        return render(request,'used_book_post.html', {'error':''})
    elif request.method == 'POST':
        param = request.POST
        name = param.get('name')
        publisher = param.get('publisher')
        course = param.get('course')
        price = param.get('price')
        seller_id = param.get('seller_id')
        seller_contact = param.get('seller_contact')
        try:
            Book.objects.create(
                name=name,
                publisher=publisher,
                course=course,
                price=price,
                seller_id=seller_id,
                seller_contact=seller_contact,
            )
        except Exception as e:
            context = {'error':e}
            return render(request,'used_book_post.html', context)
        return redirect('used_book_view')
