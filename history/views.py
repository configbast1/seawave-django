from django.shortcuts import render

def history(request):
    return render(request, 'history.html', {'title': 'Історія'})

def dates(request):
    events = [
        {'year': 2008, 'text': 'Заснування компанії в Одесі'},
        {'year': 2011, 'text': 'Перші 100 клієнтів'},
        {'year': 2014, 'text': 'Відкриття філії в Лондоні'},
        {'year': 2017, 'text': 'Відкриття філії в Парижі'},
        {'year': 2020, 'text': 'Перехід на віддалену роботу'},
        {'year': 2024, 'text': '500 працівників у штаті'},
    ]
    return render(request, 'history_dates.html', {'title': 'Історія: перелік дат', 'events': events})

def facts(request):
    return render(request, 'history_facts.html', {'title': 'Історія: значимі факти'})
