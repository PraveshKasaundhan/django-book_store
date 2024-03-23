from django.contrib import admin

from .models import Book, Author, Address, Country
# Register your models here.

admin.site.register(Country)
admin.site.register(Address)
admin.site.register(Author)

class BookAdmin(admin.ModelAdmin):
    # readonly_fields=("slug",)
    prepopulated_fields={"slug":("title",)}
    list_filter = ("title","rating","author",)
    list_display = ("title","author",)

admin.site.register(Book,BookAdmin)
