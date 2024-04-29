from atexit import register

from django.urls import path, include
from rest_framework.routers import SimpleRouter, DefaultRouter
from rest_framework_nested import routers

from catalog import views

router = DefaultRouter()
router.register("books", views.BookViewSet, "books")
router.register("authors", views.AuthorViewSet, "authors")
router.register("reviews", views.ReviewViewSet, "reviews")

image_router = routers.NestedDefaultRouter(router, "books", lookup='books')
image_router.register("images", views.ImageViewSet, "image")

review_router = routers.NestedDefaultRouter(router, "books", lookup='books')
review_router.register("reviews", views.ReviewViewSet, 'review')

urlpatterns = [
    path('', include(router.urls)),
    path('', include(review_router.urls)),
    path('', include(image_router.urls)),
    # path('books/', views.book_list),

    # path('books/', views.BookList.as_view(), name="books"),
    # path('books/<int:pk>/', views.BookDetail.as_view(), name='book_detail'),

    # path('books/<int:pk>/', views.book_details, name='book_detail'),

    # path('authors/', views.author_list),

    # path('authors/', views.AuthorList.as_view(), name="authors"),
    # path('authors/<int:pk>/', views.author_details, name='author_detail'),
    # path('authors/<int:pk>/', views.AuthorDetail.as_view(), name='author_detail'),

    path('genres/', views.genre_list),
    path('genres/<int:pk>/', views.genre_details, name='genre_detail'),

    # path('reviews/', views.review_list),
    # path('reviews/<int:pk>/', views.review_details, name='review_detail'),
]
