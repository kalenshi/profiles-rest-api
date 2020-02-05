from django.contrib import admin
from profiles_api.models import Book,Author,UserProfile

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Book)
admin.site.register(Author)
