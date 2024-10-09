from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, JsonResponse


items = [
   {"id": 1, "name": "Кроссовки abibas" ,"quantity":5},
   {"id": 2, "name": "Куртка кожаная" ,"quantity":2},
   {"id": 5, "name": "Coca-cola 1 литр" ,"quantity":12},
   {"id": 7, "name": "Картофель фри" ,"quantity":0},
   {"id": 8, "name": "Кепка" ,"quantity":124},
]


def index(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)


def about(request):
    name = 'Иван'
    surname = 'Иванов'
    patronymic = 'Петрович'
    phone = '8-923-600-01-02'
    email = 'vasya@mail.ru'

    text = f"""
        <p>Имя: <strong>{name}</strong></p>
        <p>Отчество: <strong>{patronymic}</strong></p>
        <p>Фамилия: <strong>{surname}</strong></p>
        <p>телефон: <strong>{phone}</strong></p>
        <p>email: <strong>{email}</strong></p>
    """
    return HttpResponse(text)


def get_items(request, id=None):

    ref = '<p><a href="/items">Назад к списку товаров</a></p>'

    if id is None:
        lines = '<tr><td>id</td><td>name</td><td>quantity</td><td>описание</td></tr>'
        for line in items:
            item_ref = f'<a href="/item/{line['id']}">ссылка</a>'
            lines += f'<tr><td>{line['id']}</td><td>{line['name']}</td><td>{line['quantity']}</td><td>{item_ref}</td></tr>'
        return HttpResponse(f'<table border="1">{lines}</table>' + ref)
    
    for line in items:
        if line['id'] == id:
            lines = '<tr><td>id</td><td>name</td><td>quantity</td></tr>'
            lines += f'<tr><td>{line['id']}</td><td>{line['name']}</td><td>{line['quantity']}</td></tr>'
            return HttpResponse(f'<table border="1">{lines}</table>' + ref)
    else:
        return HttpResponse(f'<p>Товар c id={id} не найден</p>' + ref)
