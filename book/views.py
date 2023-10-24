from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms

def book_view(request):
    book_value = models.Book.objects.all()
    return render(request, 'book.html', {'book_key': book_value})

def book_detail_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_key': book_id})

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