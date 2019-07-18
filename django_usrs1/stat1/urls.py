from django.urls import path

from . import views

urlpatterns = [
    path('v/', views.index, name='show')
]
