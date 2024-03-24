from django import forms
from front.models import Book, Comment, Category

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['text', 'rating']

class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'