from django.urls import path
from . import views

urlpatterns = [
    path('', views.history, name='history'),
    path('dates/', views.dates, name='history_dates'),
    path('facts/', views.facts, name='history_facts'),
]
