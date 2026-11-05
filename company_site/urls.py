from django.urls import path, include, re_path
from core.views import page_not_found

urlpatterns = [
    path('', include('core.urls')), # все делегуємо core

    # усі інші адреси, яких немає на сайті
    re_path(r'^.*$', page_not_found, name='not_found'),
]

handler404 = 'core.views.page_not_found'
