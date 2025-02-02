from django.contrib import admin

from .models import post,Author,Tag,Comment

# Register your models here.

class postAdmin(admin.ModelAdmin):
    list_filter=("Author","Tags","Date",)
    list_display=("title","Author","Date","Excerpt",)
    prepopulated_fields={"slug":("title",)}

class AuthorAdmin(admin.ModelAdmin):
    list_display=("First_Name","Last_Name",)    

class commentAdmin(admin.ModelAdmin):
    list_display=("user_name","post")    

admin.site.register(post,postAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Tag)
admin.site.register(Comment,commentAdmin)
