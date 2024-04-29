
from rest_framework import serializers
from rest_framework.relations import StringRelatedField

from catalog.models import Book, Author, Genre, Review, BookImage


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ['name']


class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = ["id", "name_of_reviewer", "book", "comment", "date"]

    def create(self, validated_date):
        book_pk = self.context['book_pk']
        return Review.objects.create(book_id=book_pk, **validated_date)


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = BookImage
        fields = ["book", "image"]


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
    # author = serializers.HyperlinkedRelatedField(
    #     queryset=Author.objects.all(),
    #     view_name='author_detail'
    # )
    author = StringRelatedField()

    class Meta:
        model = Book
        fields = ['title', 'summary', 'isbn', 'author']
