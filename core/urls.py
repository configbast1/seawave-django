from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('news/', views.news, name='news'),
    path('management/', views.management, name='management'),
    path('about/', views.about, name='about'),
    path('contacts/', views.contacts, name='contacts'),
    path('contacts/france/', views.contacts_france, name='contacts_france'),
    path('contacts/ukraine/', views.contacts_ukraine, name='contacts_ukraine'),
    path('contacts/austria/', views.contacts_austria, name='contacts_austria'),
    
    # URL для розділу "Філії" !!!
    path('branches/', include('branches.urls')),

    path('history/', include('history.urls')),
]