from django.db import models

# Create your models here.
class FLIGHT(models.Model):
    name = models.CharField(max_length=500,default="")
    gender1 = models.CharField(max_length=50,default="")
    from_city = models.CharField(max_length=50,default="")
    to_city = models.CharField(max_length=50,default="")
    from_date = models.DateField( auto_now=False, auto_now_add=False,default="")
    to_date = models.DateField( auto_now=False, auto_now_add=False,default="")
    rooms = models.BigIntegerField(default="")
    adults = models.IntegerField(default="")
    children = models.IntegerField(default="")

    def __str__(self):
        return self.name


class HOTEL(models.Model):
    name = models.CharField(max_length=500,default="")
    city = models.CharField(max_length=50,default="")
    from_date = models.DateField( auto_now=False, auto_now_add=False,default="")
    to_date = models.DateField( auto_now=False, auto_now_add=False,default="")
    rooms = models.BigIntegerField(default="")
    adults = models.IntegerField(default="")
    children = models.IntegerField(default="")
    email = models.EmailField(max_length=254,default="")
    Phone = models.IntegerField(default="")

    def __str__(self):
        return self.name

class CONTACT(models.Model):
    name = models.CharField(max_length=500,default="")
    Phone = models.IntegerField(default="")
    email = models.EmailField(max_length=254,default="")

    def __str__(self):
        return self.name


