from django.shortcuts import render
from .models import Book 
import random


def index(request):
    books = Book.objects.all()
    total_books = books.count()
    
    top3_index = ifUpdate(total_books)

    top3_books = [books[i-1] for i in top3_index]

    return render(request,"library/index.html",{
        "books":top3_books
    })

def books(request):
    all_books = Book.objects.all().order_by("-id")
    return render(request,"library/books.html",{
        "books":all_books
    })

def details(request,id):
    selected_book = Book.objects.get(id=id)

    return render(request,"library/details.html",{
        "book":selected_book
    })


def ifUpdate(total_books):
    f = open("top3.txt","r")
    list = f.read().splitlines()
     
    int_list =[]
    for i in list:
        int_list.append(int(i))
    num = int_list[0]
    old3 = int_list[1:4]
    
    print(int_list)
    
    f.close()

    if total_books != num:
        fw = open("top3.txt","w")
        fw.write(str(total_books)+'\n')
        random3 = random.sample(range(1,int(total_books)),3)
        for i in random3:
            fw.write(str(i)+'\n')
        fw.close()
        return random3
    else:
        return old3