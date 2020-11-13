from django.contrib import admin
from book_app.models import *


# Register your models here.

class BookinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'pub_date']


class HeroinfoAdmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'content', 'gender', 'book']


admin.site.register(BookInfo, BookinfoAdmin)
admin.site.register(HeroInfo, HeroinfoAdmin)
