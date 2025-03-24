from django.contrib import admin
from .models import Book

admin.site.register(Book)  # This makes the Book model appear in the Django admin