from django.shortcuts import render
from django.http import HttpResponse

from ThisisDjango.celery import add
from model.models import Animal



def test(request):

    add.delay(2,3)

    return render(request,'index.html')


def manager(request):

    m = Animal.p.all()

    print(m)

    return HttpResponse()
