from django.urls import re_path

from learn import views

urlpatterns = [
    re_path(r'test/',views.test),

    re_path(r'manager/',views.manager),
]