from django.contrib import admin
from .models import Comment, Tag, Author, Post

# Register your models here.

class PostAdmin(admin.ModelAdmin):
    list_filter = ('author', 'tag', 'date',)
    list_display = ('title', 'author', 'date',)
    prepopulated_fields = {'slug': ('title',)}



admin.site.register(Post, PostAdmin)
admin.site.register(Tag)
admin.site.register(Author)
admin.site.register(Comment)