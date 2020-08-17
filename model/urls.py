from django.conf.urls import url

from model import views

urlpatterns = [
    url(r'^index',views.index),
]