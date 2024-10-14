from django.shortcuts import render
from collections import defaultdict
# Create your views here.

from django.http import HttpResponse, HttpResponseNotFound

from MainApp.models import Item


def index(request):
    text = """
    <h1>"Изучаем django"</h1>
    <strong>Автор</strong>: <i>Иванов И.П.</i>
    """
    return HttpResponse(text)


def about(request):
    author = {
    "name": "Иван",
    "middle_name": "Петрович",
    "last_name": "Иванов",
    "phone": "8-923-600-01-02",
    "email": "vasya@mail.ru",
    }   
    return render(request, "about.html", {"author": author})


def get_item(request, item_id):
    try:
        item = Item.objects.get(id=item_id)
    except Item.DoesNotExist:
        return HttpResponseNotFound(f'Товар c id={item_id} не найден')
    else:
        context = {"item": item}
        return render(request, "item_page.html", context)


def get_items(request):
    items = Item.objects.all()
    context = {"items": items}
    return render(request, "items_list.html", context)


def home(request):
    context = {
        'name': 'Иванов Иван Иванович',
        'email': 'ivanov@mail.ru',
    }
    return render(request, 'index.html', context=context)
    
