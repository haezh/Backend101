from django.urls import path

from . import views

urlpatterns = [
    path('<str:first_name>', views.index, name='index'),
]