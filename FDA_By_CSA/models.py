from django.db import models
from django.contrib.auth.models import User

# Create your models here.

#Various Eateries at BITS
class Eatery_details(models.Model):
    Name =  models.CharField(max_length = 100)
    Location = models.CharField(max_length = 100)
#Food Item at the Eateries
class Items(models.Model):
    Food_name = models.CharField(max_length = 100)
    Price = models.DecimalField(max_digits = 8,decimal_places=2)
    Eatery = models.ForeignKey(Eatery_details,on_delete=models.CASCADE) 
#Orders placed
class Orders(models.Model):
    BITS_ID = models.ForeignKey(User,on_delete=models.CASCADE)
    Items = models.ManyToManyField(Items)
    Amount = models.DecimalField(max_digits = 8,decimal_places = 2)

#For Rating
class Rating(models.Model):
    BITS_ID = models.ForeignKey(User,on_delete=models.CASCADE)
    Item_name = models.ForeignKey(Items,on_delete=models.CASCADE)
    Rating_Points = models.PositiveIntegerField()
#For Rating_Eateries
class Rating_eatery(models.Model):
    BITS_ID = models.ForeignKey(User,on_delete=models.CASCADE)
    Eatery_name= models.ForeignKey(Eatery_details,on_delete=models.CASCADE)
    Rating_Points = models.PositiveIntegerField()   