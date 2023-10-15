from django.urls import path
from . import views

urlpatterns = [
    path('', views.book_view),
    path('book_detail/<int:id>/', views.book_detail_view),
]