from django.shortcuts import render

def history(request):
    return render(request, 'history.html', {'title': 'Історія'})

def dates(request):
    return render(request, 'history_dates.html', {'title': 'Історія: перелік дат'})

def facts(request):
    return render(request, 'history_facts.html', {'title': 'Історія: значимі факти'})
