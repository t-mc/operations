from django.db import models
from django.contrib.auth.models import User
from crm.models import Bedrijf

"""
Abstracte class voor het toevoegen van time stamp op de modellen.
"""
class TransactionDT(models.Model):
    """
    Opnemen in (vrijwel) iedere class.
    """
    created_dt = models.DateTimeField(auto_now_add=True, null=True)
    modified_dt = models.DateTimeField(auto_now=True, null=True)
    last_modified_user = models.ForeignKey('auth.User',
                                           verbose_name='Laatst gewijzigd door',
                                           null=True,
                                           blank=True, 
                                           on_delete=models.CASCADE
                                           )

    class Meta:
        abstract = True

class Productgroep(TransactionDT):
    productcode = models.CharField(max_length=10, unique=True)
    omschrijving = models.CharField(max_length=80, unique=True)
    productowner = models.ForeignKey(User, related_name='productowner', blank=True, null=True, on_delete=models.CASCADE)
    leverancier = models.ForeignKey(Bedrijf, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['productcode']
        verbose_name_plural = 'Productgroepen'

    def __str__(self):
        return self.omschrijving    


class Training(TransactionDT):
    omschrijving = models.CharField(max_length=80, unique=True)
    productgroep = models.ForeignKey(Productgroep, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        ordering = ['omschrijving']
        verbose_name_plural = 'Trainingen'

    def __str__(self):
        return self.omschrijving    