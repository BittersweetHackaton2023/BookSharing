from django.shortcuts import render
from book.models import *
from django.db.models import Q
from book.form import *
from django.http import HttpResponse
from django.core.mail import EmailMessage

## 도서 검색하기(제목, 저자, ISBN 중 1개이상의 키워드를 이용하여)
def search_books(request):
    query = request.GET.get('query')  # 검색어를 GET 파라미터로 받아옴

    # 책 검색
    books = None

    if query:
        query_parts = query.split()

        # 검색 쿼리 동적 구성
        q_objects = Q()

        for part in query_parts:
            q_objects |= Q(title__icontains=part) | Q(author__icontains=part) | Q(isbn__icontains=part)

        books = Book.objects.filter(q_objects)

    context = {
        'query': query,
        'books': books,
    }

    return render(request, 'search_results.html', context)


## email이 있는지 체크
def checkemail(email):
    try:
        member = Member.objects.get(email=email)
        return member
    except Member.DoesNotExist:
        return None


## email의 마일리지 확인
def mymileage(request):
    if request.method == 'POST':
        form = Emailform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            member = checkemail(email)
            if member:
                mileage = member.mileage
                return render(request, '.html', {'mileage': mileage})
            else:
                return render(request, '.html', {'massage': "없는 이메일입니다."})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)


## 이메일 DB에 등록
def registeremail(request):
    if request.method == 'POST':
        form = Emailform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            member = checkemail(email)
            if member:
                return render(request, '.html', {'massage': "이미 가입한 이메일입니다."})
            else:
                member = Member
                member.email = email
                member.save()
                return render(request, '.html', {'massage': "가입 되었습니다."})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)




def usemileage(request):
    if request.method == 'POST':
        form = Orderform(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            email = form.cleaned_data['email']
            mileage = form.cleaned_data['mileage']
            member = checkemail(email)
            if member:
                if member.mileage < mileage:
                    return render(request, '.html', {'massage': "마일리지가 부족합니다."})
                member.mileage -= mileage
                member.save()

                order = Order
                order.isbn = isbn
                order.email = email
                order.mileage = mileage
                order.save()
                return render(request, '.html', {'massage': mileage + " 마일리지를 사용해 신청하였습니다."})
            else:
                return render(request, '.html', {'massage': "없는 이메일입니다."})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)



def index(request):
    return render(request, 'book/index.html')

def register(request):
    return render(request, 'book/register.html')

def signup(request):
    return render(request, 'book/signup.html')