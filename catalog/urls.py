from django.urls import path

from catalog import views

urlpatterns = [
    path('books/', views.book_list),
    path('books/<int:pk>/', views.book_details, name='book_detail'),

    path('authors/', views.author_list),
    path('authors/<int:pk>/', views.author_details, name='author_detail'),

    path('genres/', views.genre_list),
    path('genres/<int:pk>/', views.genre_details, name='genre_detail'),
]
