from django.db import models


class Animal(models.Model):
    name = models.CharField(verbose_name='名字', max_length=32)
    age = models.IntegerField()

    # 所有的元信息学习
    class Meta:
        # 参数是True时不生成表
        abstract = False
        # base_manager_name = 'name'


class Student(models.Model):
    name = models.CharField(max_length=16)

    # 改变模型管理器的名字,默认是objects
    student = models.Manager()

    class Meta:
        # 用于指定模型所在的App,可以用于在其他文件下创建属于app_label的模型
        app_label = 'model'
        # base_manager_name = 's'
        db_table = 'student'
        # s = models.Manager()
