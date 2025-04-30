from django.shortcuts import render , get_object_or_404, redirect
from django.http import HttpResponse
from .models import Book, Address, Student, Department, Course, Student3, Student4, Profile
from django.db.models import Q,Count,Sum,Avg,Max,Min,Subquery, OuterRef
from .forms import BookForm, StudentForm, Student2Form, ProfileForm

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

def lab10_part1_task1(request):
    mybooks=Book.objects.order_by('title')
    return render(request, 'bookmodule/booklist_lab10.html', {'books':mybooks})

def lab10_part1_task2(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        edition = request.POST.get('edition')
        price = request.POST.get('price')

        # Optional: Add basic validation here

        Book.objects.create(
            title=title,
            author=author,
            edition=int(edition),
            price=float(price)
        )
        return redirect('lab10_part1_task1')  # Redirect to book list after adding
    return render(request, 'bookmodule/addBook.html')

def lab10_part1_task3(request , book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.title = request.POST.get('title')
        book.author = request.POST.get('author')
        book.edition = int(request.POST.get('edition'))
        book.price = float(request.POST.get('price'))
        book.save()
        return redirect('lab10_part1_task1')  # Redirect back to list after update

    return render(request, 'bookmodule/editBook.html', {'book': book})

def lab10_part1_task4(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('lab10_part1_task1')  # Redirect back to book list after deletion

def lab10_part2_task1(request):
    mybooks=Book.objects.order_by('title')
    return render(request, 'bookmodule/bookList_lab10_part2.html', {'books':mybooks})

def lab10_part2_task2(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab10_part2_task1')
        
    else:
        form = BookForm()
    return render(request,'bookmodule/part2_addBook.html', {'form': form})

def lab10_part2_task3(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        form = BookForm(request.POST, instance=book)
        if form.is_valid():
            form.save()
            return redirect('lab10_part2_task1')
    else:
        form = BookForm(instance=book)
    
    return render(request, 'bookmodule/part2_editBook.html', {'form': form, 'book': book})

def lab10_part2_task4(request, book_id):
    book = get_object_or_404(Book, pk=book_id)

    if request.method == 'POST':
        book.delete()
        return redirect('lab10_part2_task1')
    
    return render(request, 'bookmodule/part2_deleteBook.html', {'book': book})

def lab11_task1_list(request):
    mystudents=Student.objects.order_by('name')
    return render(request, 'usermodule/task1_listStudents.html', {'students':mystudents})

def lab11_task1_add(request):
    if request.method == 'POST':
        form = StudentForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab11_task1_list')
        
    else:
        form = StudentForm()
    return render(request,'usermodule/task1_addStudent.html', {'form': form})

def lab11_task1_update(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        form = StudentForm(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lab11_task1_list')
    else:
        form = StudentForm(instance=student)
    
    return render(request, 'usermodule/task1_editStudent.html', {'form': form, 'student': student})

def lab11_task1_delete(request, student_id):
    student = get_object_or_404(Student, pk=student_id)

    if request.method == 'POST':
        student.delete()
        return redirect('lab11_task1_list')
    
    return render(request, 'usermodule/task1_deleteStudent.html', {'student': student})

def lab11_task2_list(request):
    students = Student4.objects.order_by('name')
    return render(request, 'usermodule/task2_listStudents.html', {'students': students})

def lab11_task2_add(request):
    if request.method == 'POST':
        form = Student2Form(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lab11_task2_list')
    else:
        form = Student2Form()
    return render(request, 'usermodule/task2_addStudent.html', {'form': form})

def lab11_task2_update(request, student_id):
    student = get_object_or_404(Student4, pk=student_id)
    if request.method == 'POST':
        form = Student2Form(request.POST, instance=student)
        if form.is_valid():
            form.save()
            return redirect('lab11_task2_list')
    else:
        form = Student2Form(instance=student)
    return render(request, 'usermodule/task2_editStudent.html', {'form': form, 'student': student})

def lab11_task2_delete(request, student_id):
    student = get_object_or_404(Student4, pk=student_id)
    if request.method == 'POST':
        student.delete()
        return redirect('lab11_task2_list')
    return render(request, 'usermodule/task2_deleteStudent.html', {'student': student})




def profile_list(request):
    profiles = Profile.objects.all()
    return render(request, 'usermodule/profile_list.html', {'profiles': profiles})

def profile_add(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('profile_list')
    else:
        form = ProfileForm()
    return render(request, 'usermodule/profile_add.html', {'form': form})

def delete_profile(request, profile_id):
    profile = get_object_or_404(Profile, id=profile_id)

    if request.method == 'POST':
        profile.delete()
        return redirect('profile_list')

#def index(request):
    #name = request.GET.get("name") or "world!"
    #return render(request, "bookmodule/index.html" , {"name": name})  #your render line


#def index(request):
    #name = request.GET.get("name") or "world!"  #add this line
    #return HttpResponse("Hello, "+name) #replace the word “world!” with the variable name



#def index2(request, val1 = 0):   #add the view function (index2)
    #return HttpResponse("value1 = "+str(val1))
