from django.urls import path
from . import views

app_name = 'extendsapp'

urlpatterns = [
    path('', views.index, name='extend_base')

]
