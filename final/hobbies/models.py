from django.db import models

# Create your models here.
class User(models.Model):
    SEX_CHOICES = [('M', 'Male'), ('F', 'Female')]
    name = models.CharField(max_length=100)
    sex = models.CharField(max_length=1, choices=SEX_CHOICES)
    age = models.IntegerField(null=True)
    act = models.ManyToManyField('Hobbies')

    def __str__(self):
        return self.name
    

class Hobbies(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name