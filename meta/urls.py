from django.urls import re_path

from meta import views

urlpatterns = [
    re_path(r'student/', views.student)
]
