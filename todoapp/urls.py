from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ='todo-index'),
    path('update/<int:pk>', views.update, name='todo-update')
]