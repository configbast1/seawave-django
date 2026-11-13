from django.shortcuts import render, redirect
from django.urls import resolve, Resolver404
from .data import EMPLOYEES, NEWS

SECTIONS = ['news', 'management', 'about', 'contacts', 'branches', 'history']

def home(request):
    return render(request, 'home.html', {'title': 'Головна'})

def news(request):
    # складний словник: всередині ще словник і список об'єктів News
    context = {
        'title': 'Новини',
        'news_block': {
            'heading': 'Останні новини',
            'items': NEWS,
            'tags': ['офіс', 'хмара', 'навчання', 'нагороди'],
        },
    }
    return render(request, 'news.html', context)

def management(request):
    context = {
        'title': 'Керівництво компанії',
        'company': {
            'name': 'SeaWave Software',
            'founded': 2008,
            'experience': 80,
            'employees': EMPLOYEES,  # список об'єктів Employee
        },
    }
    return render(request, 'management.html', context)

def about(request):
    return render(request, 'about.html', {'title': 'Про компанію'})

def contacts(request):
    return render(request, 'contacts.html', {'title': 'Контакти'})

def contacts_france(request):
    return render(request, 'contacts_france.html', {'title': 'Контакти: Франція'})

def contacts_ukraine(request):
    return render(request, 'contacts_ukraine.html', {'title': 'Контакти: Україна'})

def contacts_austria(request):
    return render(request, 'contacts_austria.html', {'title': 'Контакти: Австрія'})

def page_not_found(request, exception=None):
    path = request.path

    # /contacts/france -> /contacts/france/
    if not path.endswith('/'):
        try:
            if resolve(path + '/').url_name != 'not_found':
                return redirect(path + '/')
        except Resolver404:
            pass

    # неіснуючий підрозділ відомого розділу -> переадресація на розділ
    section = path.strip('/').split('/')[0]
    if section in SECTIONS:
        return redirect('/' + section + '/')

    return render(request, '404.html', {'title': 'Сторінку не знайдено'}, status=404)
