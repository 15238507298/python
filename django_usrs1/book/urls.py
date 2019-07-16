from django.urls import path
from . import views

app_name = 'book'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.book, name='book'),
    path('book/detail/<book_id>', views.book_detail, name='book_detail'),
    path('bookinfo/', views.getbook_info, name='book_info')
]

