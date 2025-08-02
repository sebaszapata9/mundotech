from django.contrib import admin
from .models import Phone  # Importing the Phone model from models.py

class PhoneAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'price', 'release_date', 'new_release')  # Display these fields in the admin list view
    search_fields = ('name', 'brand')  # Enable search functionality for name and brand fields

# Register your models here.
admin.site.register(Phone, PhoneAdmin)  # Registering the Phone model to the admin site