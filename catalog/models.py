from uuid import uuid4

from django.conf import settings
from django.db import models
from django.db.models import CASCADE


# Create your models here.


# we can create the user app here, and it would enable django create a table for bookuser for us
# class BookUser(models.Model):
#     pass


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f"{self.name}"


class Book(models.Model):
    # POLITICS = 'P'
    # FINANCE = 'F'
    # ROMANCE = 'R'
    # BOOK_CHOICES = [
    #     # by using the capital letters, we're saying the values are fixed
    #     (POLITICS, 'Politics'),
    #     (FINANCE, 'Finance'),
    #     (ROMANCE, 'Romance')
    # ]

    title = models.CharField(max_length=255)
    author = models.ForeignKey('Author', on_delete=models.CASCADE)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField('Genre')

    # genre = models.CharField(max_length=1, choices=BOOK_CHOICES, default=FINANCE)
    # ForeignKey is used to denote OnetoMany

    # We can remove the author from the string when we move the author class above the book class.
    # i.e. when we declare the author class before the book class

    def __str__(self):
        return f"{self.author}{self.title} {self.isbn}"

    def list_genre(self):
        return ", ".join(genre.name for genre in self.genre.all()[:2])


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_images')
    image = models.ImageField(upload_to='')


class Author(models.Model):
    first_name = models.CharField(max_length=255, blank=True, default="", help_text="Enter your name...")
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.first_name}{self.last_name}{self.date_of_birth}{self.date_of_death}"


class Language(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.name}"


class Review(models.Model):
    name_of_reviewer = models.CharField(max_length=255, default="")
    book = models.ForeignKey(Book, on_delete=CASCADE, default="")
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name_of_reviewer} {self.comment}"


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
        return f"{self.status} {self.due_back}"
