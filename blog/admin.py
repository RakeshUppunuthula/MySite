from django.contrib import admin

from .models import post,Author,Tag

# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_filter=("Author","Tags","Date",)
    list_display=("title","Author","Date","Excerpt",)
    prepopulated_fields={"slug":("title",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display=("First_Name","Last_Name",)    

admin.site.register(post,postAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
