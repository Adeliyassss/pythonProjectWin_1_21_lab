import delete
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def book_view(request):
    book_value = models.Book.objects.all()
    return render(request, 'book.html', {'book_key': book_value})

def book_detail_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_key': book_id})

def createNewBookView(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Успешно добавленa')
    else:
        form = forms.BookForm()

    return render(request, 'create_book.html', {'form': form})

def createBookView(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h1>Комментарий успешно добавлен</h1>')
    else:
        form = forms.ReviewForm()
    return render(request, 'create_review.html', {'form': form})

def book_delete_view(request):
    lang_value = models.Book.objects.all()
    return render(request, 'book_list.html', {'lang_key': lang_value})


def book_drop_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    book_id.delete()
    return HttpResponse('Удален успешно')