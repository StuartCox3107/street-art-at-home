from django.db import models


class Blogentry(models.Model):

    class Meta:
        verbose_name_plural = 'Blogentries'

    blogposter = models.CharField(max_length=254)
    blogdate = models.DateField(null=True)
    blogid = models.DecimalField(max_digits=6, decimal_places=0)
    blogtitle = models.CharField(max_length=254)
    blogtext = models.TextField()
    blogimage_url = models.URLField(max_length=1024, null=True, blank=True)
    blogimage = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.blogtitle
