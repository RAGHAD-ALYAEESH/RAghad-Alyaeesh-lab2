from django.urls import path, re_path
from . import views
from .views import index2

urlpatterns = [
    path('', views.index),
    path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('aboutus/', views.aboutus, name="books.aboutus"),
    re_path(r'index2/(?P<val1>\w+)/$', index2),  # يقبل أي نص أو رقم
    path('html5/links',views.links, name= "links_books"),
    path('html5/text/formatting',views.text_formatting, name= "text_formatting_books"),
    path('html5/listing',views.listing, name= "listing_books"),
    path('html5/tables',views.tables, name= "tables_books"),
    path('search',views.search, name= "search_books"),
     path('booklist',views.search, name= "booklist_books"),
     path('add-book', views.add_book, name='add_book'),
     path('simple/query', views.simple_query, name='simple_query'),
    path('complex/query', views.complex_query, name='complex_query'),
       
]
## '/books/simple/query'