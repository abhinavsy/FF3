from django.contrib import admin

# Register your models here.
from .models import Author,Books


class AuthorAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Author,AuthorAdmin)

class BookAdmin(admin.ModelAdmin):
    list_display = ['name','slug','price']
    list_editable = ['price']
    prepopulated_fields = {'slug':('name',)}
admin.site.register(Books,BookAdmin)