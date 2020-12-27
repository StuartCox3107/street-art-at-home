from django.db import models

class Citiesentry(models.Model):
       
    citiesid = models.DecimalField(max_digits=6, decimal_places=0)
    citiestitle = models.CharField(max_length=254)
    citiestext = models.TextField()
    citiesimage_url = models.URLField(max_length=1024, null=True, blank=True)
    citiesimage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.blogtitle
