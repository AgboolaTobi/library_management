from rest_framework import serializers

from catalog.models import Book, Author, Genre


class GenreSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ['name']


class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = ['first_name', 'last_name', 'date_of_birth']


#
# class BookSerializer(serializers.ModelSerializer):
#     # author = AuthorSerializer()
#     # this (the above)is one way of showing relationship. A way of showing the object author in the book object.
#     )
#
#     class Meta:
#         model = Book
#         fields = ['title', 'summary', 'isbn', 'author']


class BookSerializer(serializers.ModelSerializer):
    author = serializers.HyperlinkedRelatedField(
        queryset=Author.objects.all(),
        view_name='author_detail'
    )

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']
