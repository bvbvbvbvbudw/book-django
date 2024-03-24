from django.shortcuts import render, redirect
from .models import Book, Comment, Category
from .forms import CommentForm, BookForm, CategoryForm
from django.db.models import Avg

def index(request):
    books = Book.objects.all()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)  # Передаем request.POST и request.FILES для обработки данных формы
        if form.is_valid():
            form.save()
        else:
            return render(request, 'front/index.html', {'form': form, 'books': books})
    else:
        form = BookForm()
    return render(request, 'front/index.html', {'form': form, 'books': books})


def create(request):
    form = BookForm()
    if request.method == 'POST':
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'front/create.html', {'form':form})
    else:
        return render(request, 'front/create.html', {'form': form})

def create_cat(request):
    form = CategoryForm()
    if request.method == 'POST':
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, 'front/create.html', {'form': form})
    else:
        return render(request, 'front/create.html', {'form': form})

def detail(request, pk):
    book = Book.objects.filter(id=pk).first()
    if book:
        comments = Comment.objects.filter(book=book)
        if request.method == 'POST':
            form = CommentForm(request.POST)
            if form.is_valid():
                comment = form.save(commit=False)
                comment.user = request.user  # Предполагается, что пользователь авторизован
                comment.book = book
                comment.save()

                # Пересчитываем рейтинг книги
                book.rating = Comment.objects.filter(book=book).aggregate(Avg('rating'))['rating__avg'] or 0
                book.save()

                return redirect('detail', pk=pk)  # Перенаправляем на страницу деталей книги
        else:
            form = CommentForm()
        return render(request, 'front/detail.html', {'book': book, 'comments': comments, 'form': form})
    else:
        return redirect('index')

def search(request, cat):
    book = Book.objects.filter(category__name=cat)
    return render(request, 'front/index.html', {'books': book})


def categories_processor(request):
    categories = Category.objects.all()
    return {'categories': categories}