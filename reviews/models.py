from django.db import models

# Create your models here.

class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text="Nazwa wydawnictwa.")
    website = models.URLField(help_text="Witryna wydawnictwa.")
    email = models.EmailField(help_text="Adres e-mail wydawnictwa.")
