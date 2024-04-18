from django.contrib import admin

from . import models


# Register your models here.


# class BookAdmin(admin.ModelAdmin):
#     list_display = ["title", "isbn", "author", "list_genre"]
#
#
# admin.site.register(models.Book, BookAdmin)
# admin.site.register(models.Genre)
# admin.site.register(models.Author)

# the above is the old way of doing it

@admin.register(models.Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["title", "isbn", "author", "list_genre"]
    list_per_page = 10
    list_filter = ["title"]
    search_fields = ["title", "isbn"]


@admin.register(models.Author)
class AuthorAdmin(admin.ModelAdmin):
    list_filter = ["first_name", "last_name", "date_of_birth"]
    list_per_page = 10


@admin.register(models.Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["name"]


