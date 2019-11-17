from django.db import models

# Create your models here.
class Product(models.Model): #繼承models內建的Model
    title       = models.CharField(max_length=120)
    description = models.TextField(blank=True, null=True)
    # price       = models.DecimalField(decimal_places=2,max_digits=10000)
    summary     = models.TextField()
    featured    = models.BooleanField() #blank 代表可以是空白的嗎 null代表database可以存空白嗎
