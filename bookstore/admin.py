from django.contrib import admin
from .models import Book

# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_display = ('title','price','author','category','stocks_available','stocks')
    display_links = ('title','price','author','category','stocks_available')
    readonly_fields = ('created_on',)
    ordering = ('-modified_on',)
    prepopulated_fields = {'slug':('title',)}
    # Vey hard work :( rip siam




admin.site.register(Book,BookAdmin)