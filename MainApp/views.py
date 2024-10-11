from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound


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
    href_back = '<p><a href="/items">Назад к списку товаров</a></p>'
    for item in items:
        if item['id'] == id:
            result = f"""
            <h2> Имя: {item['name']}</h2>
            <p>Количество: {item['quantity']}</p>
            {href_back}
            """
            return HttpResponse(result)
    return HttpResponseNotFound(f'<p>Товар c id={id} не найден</p>' + href_back)


def get_items(request):

    result = "<h1>Список товаров</h1><ol>"  
    
    for item in items:
        result += f'<li><a href="/item/{item['id']}">{item['name']}</a></li>'
    result += "</ol>"
    return HttpResponse(result)
    

def home(request):
    context = {
        'name': 'Иванов Иван Иванович',
        'email': 'ivanov@mail.ru',
    }
    return render(request, 'index.html', context=context)
    
