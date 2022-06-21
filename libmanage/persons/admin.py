from django.contrib import admin

# Register your models here.
from persons.models import Person, District, City, Author, Book

admin.site.register(Person)
admin.site.register(District)
admin.site.register(City)
admin.site.register(Author)
admin.site.register(Book)