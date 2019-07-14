from django.urls import path
from . import views


#定义应用空间
app_name = 'front'


urlpatterns = [
    #name 给路径起名字，可以通过reverse（name）获取url
    path('', views.index, name='index'),
    path('login', views.login, name='login')

]

