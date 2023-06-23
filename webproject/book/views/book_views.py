from django.shortcuts import render
from models.book_models import Book
from django.db.models import Q

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
