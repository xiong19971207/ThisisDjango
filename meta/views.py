from django.http import HttpResponse

from meta.models import Student


def student(request):
    s = Student.student.all()
    print(s)

    s2 = Student.student.none()
    print(s2)

    return HttpResponse('成功')
