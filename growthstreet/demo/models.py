from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import MaxValueValidator, MinLengthValidator, MaxLengthValidator, MinValueValidator

class Application(models.Model):
        SECTOR_CHOICES = (
		('R', 'Retail'),
		('PS', 'Professional Services'),
		('FD', 'Food and Drink'),
		('E', 'Entertainment'),
	)
	email = models.EmailField(unique=True)
        full_name = models.CharField(default='null', max_length=120, blank=False, null=False)
        telephone = models.IntegerField(default=0)
        purpose = models.CharField(default='null', choices=SECTOR_CHOICES, max_length=120, null=False)
	company_name = models.CharField(default='null', max_length=120, blank=False, null=False)
        company_number = models.IntegerField(default=0)
        amount = models.IntegerField(default=0, validators=[MaxValueValidator(100000), MinValueValidator(10000)])
        duration = models.IntegerField(default=0)
        timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
        updated = models.DateTimeField(auto_now_add=False, auto_now=True)

        def __unicode__(self): 
                return self.email

class Profile (models.Model):
        user = models.OneToOneField(User, on_delete=models.CASCADE)
        birthday = models.DateField(null=True, blank=True)
