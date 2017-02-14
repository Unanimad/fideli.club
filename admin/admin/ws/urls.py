from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^login/$', login, name='login'),

    url(r'^edit/$', edit, name='edit'),

    url(r'^cards/$', get_cards, name='cards'),
    url(r'^card/$', get_card, name='card'),
]
