from django.db import models
from crm.models import Bedrijf, Contactpersoon
from projecten.models import Verkoopkans
from datetime import datetime

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

class NotitieType(TransactionDT):
    notitietype = models.CharField(max_length=30, unique=True)

    class Meta:
        ordering = ['notitietype']
        verbose_name_plural = 'Notitietypen'

    def __str__(self):
        return self.notitietype    

# Create your models here.
class Notitie(TransactionDT):

    bedrijf         = models.ForeignKey(Bedrijf, blank=False, null=False, on_delete=models.CASCADE)
    contactpersoon  = models.ForeignKey(Contactpersoon, blank=True, null=True, on_delete=models.CASCADE)
    verkoopkans     = models.ForeignKey(Verkoopkans, blank=True, null=True, on_delete=models.CASCADE)
    onderwerp       = models.CharField(max_length=80, null=False, blank=False)
    notitietype     = models.ForeignKey(NotitieType, blank=True, null=True, on_delete=models.CASCADE)
    notitie         = models.CharField(max_length=512, null=True)
    datumtijd       = models.DateTimeField(default=datetime.now, blank=False)

    class Meta:
        verbose_name_plural = 'Notities'

    def __unicode__(self):
        return self.bedrijf.bedrijfsnaam + ', ' + self.onderwerp

    def __str__(self):
        return self.bedrijf.bedrijfsnaam + ', ' + self.onderwerp
  