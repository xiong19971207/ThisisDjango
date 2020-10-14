from django.db import models


# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=16,verbose_name='动物的名称')
    age = models.IntegerField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

# class Student2(models.Model):
#     id = models.AutoField(primary_key=True,null=True)
#     name = models.CharField(max_length=32)