from django.db import models

# Create your models here.
class Animal(models.Model):
    name = models.CharField(max_length=32)
    p = models.Manager()

    # class Meta:
    #     Animal.default_manager_name = 'animal'
