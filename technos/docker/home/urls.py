from django.urls import path

from . import views

# from home.dash_apps.finished_apps import simpleexample

urlpatterns = [
    path(r'index/', views.index, name='index'),
    ]

