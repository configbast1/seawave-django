from django.shortcuts import render, redirect
from django.urls import resolve, Resolver404

SECTIONS = ['news', 'management', 'about', 'contacts', 'branches', 'history']

def home(request):
    return render(request, 'home.html', {'title': 'Головна'})

def news(request):
    return render(request, 'news.html', {'title': 'Новини'})

def management(request):
    return render(request, 'management.html', {'title': 'Керівництво компанії'})

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
