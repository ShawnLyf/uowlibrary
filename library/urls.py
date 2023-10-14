from django import views
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name = "index_page"),
    path("books",views.books,name = "books_page"),
    path("books/<int:id>",views.details,name = "deatils_page")
]