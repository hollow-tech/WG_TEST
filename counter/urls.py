from django.urls import path
from .views import list, render_csv


urlpatterns = [
    path('', list, name='list'),
    path('table/', render_csv, name='table')
]

