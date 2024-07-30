from django.shortcuts import render 
from bookapp.models import Book
from  django.shortcuts import redirect

# Create your views here.
def home(request):
    context={}
    context['num1']=100
    context['name']='aditi'
    context['num2']=150
    context['data']=[10,20,30,40]
    return render(request, 'index.html',context)

def addbook(request):
    return render(request,'addbook.html')

def booklist(request):
    context={}
    data = Book.objects.all()
    print(type(data))
    context['books']=data
    return render(request,'allbooks.html',context)

def savebook(request):
    #using GET
    #print(request.method)
    #t = request.GET['title']
    #a = request.GET['author']
    #p = request.GET['price']
    #print((type(t), (type)(a), (type)(p))
    
        
    #print(request.method)
    # using POST
    #print(request.method)
    t = request.POST['title']
    a = request.POST['author']
    p = int(request.POST['price'])
    print(t,a,p)
    print(type(t), type(a), type(p))
    b=Book.objects.create(title=t, author=a,price=p)
    #print("book added")
    b.save()
    #return render(request,'index.html')
    return redirect('/list')
    

def deleteBook(request,rid):
     book = Book.objects.filter(id=rid)
     print(book)
     book.delete()
     #context={'success': 'Book deleted!!'}
     #return render(request,'allbooks.html',context)
     return redirect('/list')
 
def editBook(request,rid):
     book = Book.objects.filter(id=rid)#book is a single object
     print(book)#queryset holding a single object
     context={}
     if request.method == "GET":
        context['book']=book[0]
        return render(request,'editbook.html',context)
     else: #POST
         t=request.POST['title']
         a=request.POST['author']
         p=int(request.POST['price'])
         book.update(title=t, author=a, price=p) #update can be called on query set
         return redirect('/list')
     
     
     