from django.shortcuts import render, redirect
from book.models import *
from django.db.models import Q, Count
from book.form import *
from django.http import HttpResponse
from datetime import datetime, timedelta
from django.core.exceptions import ObjectDoesNotExist

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
                return render(request, 'book/mymileage.html', {'mileage': mileage})
            else:
                return render(request, 'book/mymileage.html', {'massage': "메일이 존재하지 않습니다."})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, 'book/mymileage.html', context)



## 이메일 DB에 등록x
def registeremail(request):
    if request.method == 'GET':
        form = Emailform(request.GET.get('email',None))
        print(form) 
        
        if form.is_valid():
            email = form.cleaned_data['email']
            member = checkemail(email)
            if member:
                return render(request, 'book/signup.html', {'massage': "이미 가입한 이메일입니다."})
            else:
                member = Member
                member.email = email
                member.save()
                return render(request, 'book/signup.html', {'massage': "가입 되었습니다."})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, '.html', context)


##경매 신청(신청자들의 정보(마일리지 기준)를 내림차순으로 저장)
def usemileage(request):
    if request.method == 'POST':
        form = Mileageform(request.POST)
        form = Orderform(request.POST)
        if form.is_valid():
            isbn = form.cleaned_data['isbn']
            email = form.cleaned_data['email']
            mileage = form.cleaned_data['mileage']
            
            # 회원 정보 가져오기
            try:
                member = Member.objects.get(email=email)
            except ObjectDoesNotExist:
                return render(request, 'mileage_usage.html', {'error_message': '해당 이메일로 등록된 회원이 없습니다.'})
            
            # 마일리지 차감
            if member.mileage >= mileage:
                member.mileage -= mileage
                member.save()
                
            # 경매 신청자들의 마일리지를 내림차순으로 저장
            participants = AuctionParticipant.objects.order_by('-mileage')
            
            return render(request, 'mileage_usage.html', {'mileage': mileage, 'participants': participants})
    else:
        form = Emailform()
    
    context = {'form': form}
    return render(request, 'mileage_usage.html', context)


def index(request):
    return render(request, 'book/index.html')

def register(request):
    return render(request, 'book/register.html')

def signup(request):
    return render(request, 'book/signup.html')


##경매에 도서를 등록(+ 경매 시간)
def register_auction(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            book_title = form.cleaned_data['title']
            
            # 동일한 도서가 이미 등록되어 있는지 확인
            if Book.objects.filter(title=book_title).exists():
                # 이미 등록된 도서인 경우
                book = Book.objects.get(title=book_title)
            else:
                # 도서 등록 시간
                auction_start_time = datetime.now()
                # 경매 종료 시간
                auction_end_time = auction_start_time + timedelta(hours=24)
                
                # 새로운 도서 등록
                book = form.save(commit=False)
                book.auction_start_time = auction_start_time
                book.auction_end_time = auction_end_time
                book.save()

            # 등록자 정보 저장
            participant = AuctionParticipant(user=request.user, email=email, mileage=0, auction_time=datetime.now())
            participant.save()

            return redirect('auction_list')
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'register_auction.html', context)



##경매에 등록된 도서별 개수 현황
def get_book_counts():
    book_counts = Book.objects.values('title').annotate(count=Count('title'))
    return book_counts
'''
사용예시
book_counts = get_book_counts()
for book in book_counts:
    title = book['title']
    count = book['count']
    print(f"{title}: {count}")

'''