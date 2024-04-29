import segno
from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.filters import SearchFilter
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet

from .models import Book, Author, Genre, Review
from .pagination import DefaultPagination
from .permissions import IsAdminOrReadOnly
from .serializers import AuthorSerializer, BookSerializer, GenreSerializer, ReviewSerializer


# Create your views here.


# How to convert function based views to class based views
# When to use a function based view and when to use a class based view

# We can also use the ListCreatAPIView


# class BookList(ListCreateAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#
#
# class BookDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer


# We can also use the viewset to combine the booklist and bookdetail.

class BookViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    pagination_class = DefaultPagination
    permission_classes = [IsAdminOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fileds = ["title", "summary"]


# class AuthorList(ListCreateAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer
#
#
# class AuthorDetail(RetrieveUpdateDestroyAPIView):
#     queryset = Author.objects.all()
#     serializer_class = AuthorSerializer

class AuthorViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [IsAuthenticated]
    filter_backends = [SearchFilter]
    search_fields = ['first_name', 'last_name']
    ordering_fields = ['first_name']


class ReviewViewSet(ModelViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        return Review.objects.filter(book_id=self.kwargs['book_pk'])

    def get_serializer_class(self):
        return {'book_pk': self.kwargs['book_id']}


#
# class BookList(APIView):
#     def post(self, request):
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#
#         return Response(serializer.data, status=status.HTTP_201_CREATED)

#
# class BookDetail(APIView):
#     def get(self, request, pk):
#         book = get_object_or_404(Book, id=pk)
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         book = get_object_or_404(Book, id=pk)
#         serializer = BookSerializer(book, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, pk):
#         book = get_object_or_404(Book, id=pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#
# class AuthorList(APIView):
#     def post(self, request):
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#     def get(self, request):
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# class AuthorDetail(APIView):
#     def get(self, request, pk):
#         author = get_object_or_404(Author, id=pk)
#         serializer = AuthorSerializer(author)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def put(self, request, pk):
#         author = get_object_or_404(Author, id=pk)
#         serializer = AuthorSerializer(author, data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     def delete(self, request, pk):
#         author = get_object_or_404(Author, id=pk)
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def genre_list(request):
    if request.method == 'GET':
        genres = Genre.objects.all()
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = GenreSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(["GET", "PUT", "DELETE"])
def genre_details(request, pk):
    genre = get_object_or_404(Genre, id=pk)
    if request.method == "GET":
        serializer = GenreSerializer(genre)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "PUT":
        serializer = GenreSerializer(genre)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == "DELETE":
        genre.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET', 'POST'])
# def review_list(request):
#     if request.method == 'GET':
#         reviews = Review.objects.all()
#         serializer = ReviewSerializer(reviews, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = ReviewSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def review_details(request, pk):
#     review = get_object_or_404(Review, id=pk)
#     if request.method == "GET":
#         serializer = ReviewSerializer(review)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "PUT":
#         serializer = ReviewSerializer(review)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "DELETE":
#         review.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# @api_view(['GET', 'POST'])
# def book_list(request):
#     if request.method == 'GET':
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True, context={'request': request})
#         return Response(serializer.data, status=status.HTTP_200_OK)
#     elif request.method == 'POST':
#         serializer = BookSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def book_details(request, pk):
#     book = get_object_or_404(Book, id=pk)
#     if request.method == "GET":
#         serializer = BookSerializer(book)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "PUT":
#         serializer = BookSerializer(book)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "DELETE":
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

#
# @api_view(['GET', 'POST'])
# def author_list(request):
#     if request.method == 'GET':
#         authors = Author.objects.all()
#         serializer = AuthorSerializer(authors, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "POST":
#         serializer = AuthorSerializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#
#
# @api_view(["GET", "PUT", "DELETE"])
# def author_details(request, pk):
#     author = get_object_or_404(Author, id=pk)
#     if request.method == "GET":
#         serializer = AuthorSerializer(author)
#         author_qrcode = segno.make_qr("Welcome to Django")
#         author_qrcode.save("welcome.png")
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "PUT":
#         serializer = AuthorSerializer(author)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_200_OK)
#
#     elif request.method == "DELETE":
#         author.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
