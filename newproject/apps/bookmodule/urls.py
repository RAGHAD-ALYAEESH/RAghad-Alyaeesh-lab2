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
    path('lab8/task1', views.lab8_task1 , name='lab8_task1'),
    path('lab8/task2', views.lab8_task2 , name='lab8_task2'),
    path('lab8/task3', views.lab8_task3 , name='lab8_task3'),
    path('lab8/task4', views.lab8_task4 , name='lab8_task4'),
    path('lab8/task5', views.lab8_task5 , name='lab8_task5'),
    path('lab8/task7', views.lab8_task7 , name='lab8_task7'),
    path('lab9/task1', views.lab9_task1 , name='lab9_task1'),
    path('lab9/task2', views.lab9_task2 , name='lab9_task2'),
    path('lab9/task3', views.lab9_task3 , name='lab9_task3'),
    path('lab9/task4', views.lab9_task4 , name='lab9_task4'),

          
]
## '/books/simple/query'