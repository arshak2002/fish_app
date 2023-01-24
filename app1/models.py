from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Display(models.Model):
    image = models.ImageField(upload_to='fishes')
    name = models.CharField(max_length=220)
    weight = models.IntegerField()
    price = models.IntegerField()

    def __str__(self) :
        return self.name

class Orders(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    place = models.CharField(max_length=200)
    ph_number = models.IntegerField()
    qty = models.IntegerField()

    def __str__(self) :
        return self.name

class Feedbacks(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    feedback = models.TextField()


