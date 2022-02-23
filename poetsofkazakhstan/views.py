from datetime import datetime
from django.shortcuts import render
from django.http import *

from .models import *

menu = [{'title': "Home", 'url_name': 'index'},
        {'title': "Categories", 'url_name': 'categories'},
        {'title': "About", 'url_name': 'about'},
        {'title': "Contacts", 'url_name': 'contacts'}
        ]


def get_year():
    year = datetime.today().year
    return year


def get_poets():
    poets = Poets.objects.all()
    return poets


def get_poems():
    poems = Poems.objects.all()
    return poems


def get_categories():
    categories = Categories.objects.all()
    return categories


def get_info():
    info = Informations.objects.all()
    return info


def index(request):
    context = {
        'poets': get_poets(),
        'categories': get_categories(),
        'menu': menu,
        'title': 'Poets of Kazakhstan',
    }
    return render(request, 'poetsofkazakhstan/index.html', context=context)


def categories(request):
    context = {
        'poets': get_poets(),
        'categories': get_categories(),
        'menu': menu,
        'title': 'Poets of Kazakhstan',
    }
    return render(request, 'poetsofkazakhstan/categories.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'categories': get_categories(),
        'title': 'PoKZ - About',
        'year': get_year()
    }
    return render(request, 'poetsofkazakhstan/about.html', context=context)


def contacts(request):
    context = {
        'menu': menu,
        'categories': get_categories(),
        'title': 'PoKZ - Contacts',
    }
    return render(request, 'poetsofkazakhstan/contacts.html', context=context)


def show_poems(request, poem_id):
    context = {
        'poets': get_poets(),
        'categories': get_categories(),
        'menu': menu,
        'title': f'Poets of Kazakhstan - {poem_id}',
        'poems': get_poems(),
        'poem_id': poem_id
    }
    return render(request, 'poetsofkazakhstan/poems.html', context=context)


def show_poets(request, poet_id):
    context = {
        'poets': get_poets(),
        'menu': menu,
        'title': f'Poets of Kazakhstan - {poet_id}',
        'poet_id': poet_id,
        'poems': get_poems(),
        'informations': get_info()
    }
    return render(request, 'poetsofkazakhstan/poets.html', context=context)


def show_category(request, category_id):
    context = {
        'poets': get_poets(),
        'categories': get_categories(),
        'menu': menu,
        'category_id': category_id,
        'title': f'Poets of Kazakhstan',
        'poems': get_poems()
    }
    return render(request, 'poetsofkazakhstan/category_view.html', context=context)


def pageNotFound(request, exception):
    return HttpResponseNotFound("<h1>Sorry, page not found</h1>")
