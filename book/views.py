import delete
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from . import models, forms
from django.views import generic

class BookView(generic.ListView):
    template_name = 'book.html'
    queryset = models.Book.objects.all()

    def get_queryset(self):
        return models.Book.objects.all()


class BookDetailView(generic.DetailView):
    template_name = 'book_detail.html'

    def get_object(self, **kwargs):
       book = self.kwargs.get('id')
       return get_object_or_404(models.Book, id=book)


class CreateNewBookView(generic.CreateView):
    template_name = 'create_book.html'
    form_class = forms.BookForm
    queryset = models.Book.objects.all()
    success_url = '/'

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateNewBookView, self).form_valid(form=form)

class UpdateBookView(generic.UpdateView):
    template_name = 'update_book.html'
    form_class = forms.BookForm
    success_url = '/'

    def get_object(self, **kwargs):
        book = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book)

    def form_valid(self, form):
        return super(UpdateBookView, self).form_valid(form=form)

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

class BookDropView(generic.DeleteView):
    template_name = 'confirm_delete.html'
    success_url = '/'

    def get_object(self, **kwargs):
        book_id = self.kwargs.get('id')
        return get_object_or_404(models.Book, id=book_id)

class SearchView(generic.ListView):
    template_name = 'book.html'
    context_object_name = ('book')
    paginate_by = 5

    def get_queryset(self):
        return models.Book.objects.filter(title__icontains=self.request.GET.get('q'))

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        return context