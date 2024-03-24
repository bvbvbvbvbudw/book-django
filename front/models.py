from django.db import models
from django.contrib.auth.models import User


# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.CharField(max_length=100)
    pages = models.IntegerField()
    preview = models.FileField(upload_to='static/uploads', null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    file = models.FileField(upload_to='static/uploads/books/')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    rating = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

class CommentLike(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.ForeignKey(Comment, on_delete=models.CASCADE, related_name='likes')

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CategoryBook(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='category')
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book')