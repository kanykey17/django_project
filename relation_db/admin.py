from django.contrib import admin
from .models import Category, Person, Tour, Registration, Review

admin.site.register(Category)
admin.site.register(Person)
admin.site.register(Tour)
admin.site.register(Registration)
admin.site.register(Review)
