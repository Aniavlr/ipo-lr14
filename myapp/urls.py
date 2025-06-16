from django.urls import path
from .views import main_page, about, ofiston, spec_list, spec_detail

urlpatterns = [
    # path('', main_page, name ='main_page'),
    # path('',about, name='about_page'),
    # path('',ofiston,name='ofiston_page'),
    path('', main_page, name ='main_page'),
    path('about/',about, name='about_page'),
    path('officeton/',ofiston,name='ofiston_page'),
    path('spec_list/', spec_list, name='spec_list_page'),
    path('spec/<int:id>/', spec_detail, name='spec_detail_page'),
]