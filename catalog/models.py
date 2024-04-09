from uuid import uuid4

from django.db import models

from django.conf import settings


# Create your models here.


# we can create the user app here, and it would enable django create a table for bookuser for us
# class BookUser(models.Model):
#     pass


class Book(models.Model):
    POLITICS = 'P'
    FINANCE = 'F'
    ROMANCE = 'R'
    BOOK_CHOICES = [
        # by using the capital letters, we're saying the values are fixed
        (POLITICS, 'Politics'),
        (FINANCE, 'Finance'),
        (ROMANCE, 'Romance')
    ]
    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=10)
    genre = models.CharField(max_length=1, choices=BOOK_CHOICES, default=FINANCE)
    # ForeignKey is used to denote OnetoMany

    # We can remove the author from the string when we move the author class above the book class.
    # i.e. when we declare the author class before the book class

    def __str__(self):
        return f"{self.title} {self.isbn}"


class Author(models.Model):
    name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.name}"


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class BookInStance(models.Model):
    UNAVAILABLE = 'U'
    AVAILABLE = 'A'
    LOAN_STATUS = [
        # by using the capital letters, we're saying the values are fixed
        (UNAVAILABLE, 'U'),
        (AVAILABLE, 'A')
    ]
    unique_id = models.UUIDField(default=uuid4, primary_key=True)
    due_back = models.DateTimeField()
    status = models.CharField(max_length=1, choices=LOAN_STATUS, default=AVAILABLE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.LOAN_STATUS}"
