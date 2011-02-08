from django.contrib import admin
from blog.models import *

class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'slug', 'description')
    search_fields = ['title']

class PostAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("title",)}
    list_display = ('title', 'pub_date', 'status')
    list_filter = ['status']
    search_fields = ['title']

admin.site.register(Category, CategoryAdmin)
admin.site.register(Post, PostAdmin)