from django.urls import path
from . import views

app_name = 'singlepage'

urlpatterns = [
    # path('', views.index, name = 'index'),
    path('<str:name>', views.hello, name = 'hello'),
]
