from django.contrib import admin
from front.models import Book, Comment, CommentLike, CategoryBook, Category

# Register your models here.
admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(CommentLike) # need delete
admin.site.register(Category)
admin.site.register(CategoryBook)