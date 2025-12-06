from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime

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

from django.core.validators import MinValueValidator, MaxValueValidator, MinLengthValidator

