from django.urls import path, re_path
from . import views
from .views import index2

urlpatterns = [
    path('', views.index),
   re_path(r'index2/(?P<val1>\w+)/$', index2),  # يقبل أي نص أو رقم
   path('<int:bookId>', views.viewbook),
    path('', views.index, name= "books.index"),
    path('list_books/', views.list_books, name= "books.list_books"),
    path('<int:bookId>/', views.viewbook, name="books.view_one_book"),
    path('aboutus/', views.aboutus, name="books.aboutus"),


]
