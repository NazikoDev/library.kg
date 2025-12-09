from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
from .models import Book

def writersView(request):
    if request.method == 'GET':
        return HttpResponse("ПИСАТЕЛИ КР<br>"
        "<br>"
        "Чингиз Айтматов<br>"
        "Токтоболот Абдумомунов<br>"
        "Касымалы Баялинов<br>"
        "Тологон Касымбеков<br>"
        "Түгөлбай Сыдыкбеков<br>"
        "Касымалы Джантошев<br>"
        "Аалы Токомбаев<br>"
        "Мелис Абакиров<br>"
        "Казат Акматов<br>"
        "Шаршеналы Абдылдаев")


def quotesView(request):
    if request.method == 'GET':
        return HttpResponse("ЦИТАТЫ<br>"
          "Жизнь — это путешествие, а не пункт назначения.<br>"
          "Чем умнее человек, тем легче он признает себя дураком.<br>"
          "Чтобы чего-то достичь, нужно перестать говорить и начать действовать.<br>"
          "Будущее принадлежит тем, кто верит в красоту своей мечты.<br>"
          "«Я знаю, что ничего не знаю.»<br>")


def timeView(request):
    if request.method == "GET":
        now = datetime.now().strftime("%H:%M:%S")    #type:ignore
        return HttpResponse(now)


def books_listView(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})

def book_detailView(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})

