from django.urls import path
from . import views
app_name = 'dateapp'

urlpatterns = [
    path('', views.index, name='dateindex')

]

