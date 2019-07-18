from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('show_book/<int:book_id>', views.book_detail, name='show_book'),
    path('add_book/', views.add_book, name='add_book'),
    path('delete_book/', views.delete_book, name='delete_book')

]

