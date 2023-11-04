from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookView.as_view()),
    path('book_detail/<int:id>/', views.BookDetailView.as_view()),
    path('add-comment/', views.createBookView),
    path('create_new_book/', views.CreateNewBookView.as_view()),
    path('book_list/<int:id>/delete/', views.BookDropView.as_view()),
    path('book_list/<int:id>/update/', views.UpdateBookView.as_view()),
    path('seacrh/', views.SearchView.as_view(), name='search'),
]