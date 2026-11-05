from django.shortcuts import render

def branches_list(request):
    return render(request, 'branches_list.html', {'title': 'Филиалы'})

def london(request):
    return render(request, 'london.html', {'title': 'Філія в Лондоні'})

def paris(request):
    return render(request, 'paris.html', {'title': 'Філія в Парижі'})