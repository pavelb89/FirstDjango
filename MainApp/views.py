from django.shortcuts import render
from collections import defaultdict
# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity": 5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity": 2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity": 12},
   {"id": 7, "name": "Картофель фри" ,"quantity": 0},
   {"id": 8, "name": "Кепка" ,"quantity": 124},
]


def index(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)


def about(request):
    author = {
        'Имя': 'Иван',
        'Фамилия': 'Иванов',
        'Отчество': 'Петрович',
        'Телефон': '8-923-600-01-02',
        'email': 'vasya@mail.ru',
    }
    

    text = f"""
        Имя: <i>{author['Имя']}</i><br>
        Отчество: <i>{author['Фамилия']}</i><br>
        Фамилия: <i>{author['Отчество']}</i><br>
        телефон: <i>{author['Телефон']}</i><br>
        email: <i>{author['email']}</i>
    """
    return HttpResponse(text)


def get_item(request, id):
    for item in items:
        if item['id'] == id:
            return render(request, 'item.html', item)
    return HttpResponseNotFound(f'<p>Товар c id={id} не найден</p>' + href_back)


def get_items(request):
    context = {"items": items}
    return render(request, "items_list.html", context)


def home(request):
    context = {
        'name': 'Иванов Иван Иванович',
        'email': 'ivanov@mail.ru',
    }
    return render(request, 'index.html', context=context)
    
