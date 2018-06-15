from django.urls import path
from django.conf.urls import url ## FIXME url/pathの違い

from . import views

urlpatterns = [
    path('', views.hello, name='hello'),  ## /hello
    url(r'^index$', views.index, name='index'), ## /hello/index
]
