from django.shortcuts import render, redirect
from models.book_models import Book
from django.db.models import Q
from webproject.book.form import BookForm

def search_books(request):
    """
    도서 검색 기능을 처리하는 함수.
    사용자가 제목, 저자, ISBN 중 하나 이상의 키워드를 입력하여 도서를 검색할 수 있음.

    :param request: 요청 객체
    :return: 검색 결과를 포함한 템플릿 렌더링 결과
    """
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


def register(request):
    """
    도서 등록 기능을 처리하는 함수.
    사용자가 도서 정보를 입력하여 등록할 수 있음.

    :param request: 요청 객체
    :return: 도서 등록 후 도서 리스트 페이지로 리다이렉트
    """
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            # 폼 데이터 유효성 검사를 통과한 경우
            book = form.save()  # 도서 정보 저장
            return redirect('book_list')  # 도서 리스트 페이지로 리다이렉트
    else:
        form = BookForm()

    context = {'form': form}
    return render(request, 'register.html', context)


def book_list(request):
    """
    도서 목록을 표시하는 함수.
    등록된 모든 도서 정보를 가져와서 템플릿에 전달함.

    :param request: 요청 객체
    :return: 도서 목록을 포함한 템플릿 렌더링 결과
    """
    books = Book.objects.all()  # 모든 도서 정보 가져오기

    context = {'books': books}
    return render(request, 'book_list.html', context)
