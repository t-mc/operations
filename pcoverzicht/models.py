from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Computer(models.Model):
    naam = models.CharField(max_length=40, unique=True)
    gebruiker = models.CharField(max_length=80)
    merkentype = models.CharField('Merk en Type', max_length=80)
    kenmerken = models.TextField()
    aanschafdatum = models.DateField()
    serienummer = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name_plural = "Computers"

    def __str__(self):
        return self.naam

    def get_absolute_url(self):
        return reverse('computer_edit', kwargs={'pk': self.pk})


class Software(models.Model):
    naam = models.ForeignKey(Computer, verbose_name='PC Naam', null= False)
    software = models.CharField(max_length=80, null=False)
    versienummer = models.CharField(max_length=20)
    productkey = models.CharField(max_length=40, blank=True)

    class Meta:
        verbose_name_plural = "Software"

    # def __str__(self):
    #     return self.pk

    def get_absolute_url(self):
        return reverse('software_edit', kwargs={'pk': self.pk})

