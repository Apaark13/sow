from django.contrib import admin

# Register your models here.
from .models import Term, PriceList

admin.site.register(Term)
admin.site.register(PriceList)