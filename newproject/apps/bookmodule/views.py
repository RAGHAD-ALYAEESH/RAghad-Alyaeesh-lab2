from django.shortcuts import render
from django.http import HttpResponse
from .models import Book,Address,Student,Department,Course,Student3
from django.db.models import Q,Count,Sum,Avg,Max,Min,Subquery, OuterRef

def index(request): 
    name = request.GET.get("name") or "world!"
    #return render(request, "bookmodule/index.html")
    return render(request, "bookmodule/index.html" , {"name": name})  #your render line

def index2(request, val1):   #add the view function (index2)
    if val1.isdigit():  
        return HttpResponse("value1 = " + val1)
    else:
        return HttpResponse("error, expected val1 to be integer")
    
def viewbook(request, bookId):
    # assume that we have the following books somewhere (e.g. database)
    book1 = {'id':123, 'title':'Continuous Delivery', 'author':'J. Humble and D. Farley'}
    book2 = {'id':456, 'title':'Secrets of Reverse Engineering', 'author':'E. Eilam'}
    targetBook = None
    if book1['id'] == bookId: targetBook = book1
    if book2['id'] == bookId: targetBook = book2
    context = {'book':targetBook} # book is the variable name accessible by the template
    return render(request, 'bookmodule/show.html', context)

def index(request):
    return render(request, "bookmodule/index.html")
 
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
 
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
 
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def text_formatting(request):
    return render(request, 'bookmodule/text_formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')

def search(request):
    if request.method == "POST":
        string = request.POST.get('keyword').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')
        # now filter
        books = __getBooksList()
        newBooks = []
        for item in books:
            contained = False
            if isTitle and string in item['title'].lower(): contained = True
            if not contained and isAuthor and string in item['author'].lower():contained = True
            
            if contained: newBooks.append(item)
        return render(request, 'bookmodule/bookList.html', {'books':newBooks})

    return render(request, 'bookmodule/search.html')

def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]

def add_book(request):
    mybook = Book(title='Continuous Delivery', author='J.Humble and D. Farley', edition=1, price=120.00)
    mybook.save()  # Save the book to the database
    mybook = Book.objects.create(title = 'undercover acadimec proffesor', author = 'sherlock HOlmes', edition = 1)
    return render(request, 'book_added.html', {'book': mybook})  # Render a response

def simple_query(request):
    mybooks=Book.objects.filter(title__icontains='and') # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def complex_query(request):
    mybooks=books=Book.objects.filter(author__isnull = False).filter(title__icontains='and').filter(edition__gte = 2).exclude(price__lte = 100)[:10]
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')

def lab8_task1(request):
    mybooks=Book.objects.filter(Q (price__lte=80)) # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lab8_task2(request):
    mybooks=Book.objects.filter(Q (edition__gt = 3)&(Q(author__icontains = 'co')|Q(title__icontains='co'))) # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lab8_task3(request):
    mybooks=Book.objects.filter(Q (edition__lte = 3)&(~Q(author__icontains = 'co')|~Q(title__icontains='co'))) # <- multiple objects
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lab8_task4(request):
    mybooks=Book.objects.order_by('title')
    return render(request, 'bookmodule/bookList.html', {'books':mybooks})

def lab8_task5(request):
    stats=Book.objects.aggregate(
       total_books=Count('id'),
       total_price=Sum('price'),
       average_price=Avg('price'),
       max_price=Max('price'),
       min_price=Min('price')
    )
    return render(request, 'bookmodule/static.html', {'stats':stats})

def lab8_task7(request):
    city_stats = Address.objects.annotate(student_count=Count('student')) 
    return render(request, 'bookmodule/student.html', {'city_stats': city_stats})


def lab9_task1(request):
    name_of_Dep = Department.objects.annotate(student_count=Count('student3')) .order_by('-student_count')
    return render(request, 'bookmodule/department.html', {'name_of_Dep': name_of_Dep})


def lab9_task2(request):
    name_of_Course = Course.objects.annotate(student_count=Count('student3')) .order_by('-student_count')
    return render(request, 'bookmodule/course.html', {'name_of_Course': name_of_Course})

def lab9_task3(request):
     departments = Department.objects.annotate(
       oldest_student_id=Min('student3__id')
      )
     return render(request, 'bookmodule/min_student.html', {'departments': departments})

def lab9_task4(request):
    departments = Department.objects.annotate(student_count=Count('student3')) \
        .filter(student_count__gt=2) \
        .order_by('-student_count')

    return render(request, 'bookmodule/student_GT_2.html', {'departments_with_more_than_two': departments})






















#def index(request):
    #name = request.GET.get("name") or "world!"
    #return render(request, "bookmodule/index.html" , {"name": name})  #your render line


#def index(request):
    #name = request.GET.get("name") or "world!"  #add this line
    #return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name



#def index2(request, val1 = 0):   #add the view function (index2)
    #return HttpResponse("value1 = "+str(val1))
