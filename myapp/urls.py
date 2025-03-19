from django.urls import path
from .views import main_page, about, ofiston

urlpatterns = [
    path('', main_page, name ='main_page'),
    path('',about, name='about_page'),
    path('',ofiston,name='ofiston_page'),
]