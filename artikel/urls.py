from django.urls import path
from artikel.views import *

app_name = 'artikel'

urlpatterns = [
    path('', show_artikel, name='show_artikel'),
    path('json/', show_json, name='show_json'),
    path('add/',create_article_AJAX, name='create_article_AJAX'),
    path('delete/<int:id>/', delete, name='delete'),
    path('full-article/<int:id>/',full_article, name='full_article'),
]