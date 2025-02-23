from django.urls import path, re_path
from . import views
from .views import index2

urlpatterns = [
    path('', views.index),
   re_path(r'index2/(?P<val1>\w+)/$', index2),  # يقبل أي نص أو رقم
   path('<int:bookId>', views.viewbook),


]
