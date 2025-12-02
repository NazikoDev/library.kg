from django.urls import path
from . import views

urlpatterns = [
    path('writers/', views.writersView, name='writers'),    #type:ignore
    path('quotes/', views.quotesView, name='quotes'),       #type:ignore
    path('time/', views.timeView, name='time'),             #type:ignore 
]
