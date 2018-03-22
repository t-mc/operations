from django.db import models
from django.contrib.auth.models import User

from crm.models import Bedrijf, Contactpersoon
from producten.models import Productgroep

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

class Verkoopstadium(TransactionDT):
    verkoopstadium = models.CharField(max_length=30, unique=True)
    verkoopkans = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['verkoopstadium']
        verbose_name_plural = 'Verkoopstadia'

    def __str__(self):
        return self.verkoopstadium    

class Orderstadium(TransactionDT):
    orderstadium = models.CharField(max_length=30, unique=True)
    order = models.DecimalField(max_digits=4, decimal_places=2)

    class Meta:
        ordering = ['orderstadium']
        verbose_name_plural = 'Orderstadia'

    def __unicode__(self):
        return self.orderstadium    

class Verkoopkans(TransactionDT):

    projectcode = models.CharField(max_length=10, unique=False)
    omschrijving = models.CharField(max_length=256, null=False, blank=False)
    bedrijf = models.ForeignKey(Bedrijf, null=False, blank=False, on_delete=models.CASCADE)
    opdrachtgever = models.ForeignKey(Contactpersoon, blank=True, null=True, on_delete=models.CASCADE)
    verkoopstadium = models.ForeignKey(Verkoopstadium, related_name='Verkoop_Stadium', null=False, blank=False, on_delete=models.CASCADE)
    startdatum_project = models.DateField(blank=True, null=True)
    einddatum_project = models.DateField(blank=True, null=True)
    onenote_doc = models.URLField(blank=True, null=True)
    klantpartner = models.ForeignKey(User, related_name='Verkoopkans_Klantpartner', blank=True, null=True, on_delete=models.CASCADE)
    ordereigenaar = models.ForeignKey(User, related_name='Verkoopkans_Ordereigenaar', blank=True, null=True, on_delete=models.CASCADE)
    productgroep = models.ForeignKey(Productgroep, related_name='Verkoopkans_Productgroep', blank=True, null=True, on_delete=models.CASCADE)
    actief = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Verkoopkansen'
        ordering = ['-modified_dt']

    def __unicode__(self):
        return self.projectcode    

    def __str__(self):
        return self.projectcode    

class Orders(Verkoopkans):
    class Meta:
        verbose_name_plural = 'Orders'
        proxy = True

class Order(TransactionDT):
    
    projectcode = models.CharField(max_length=10, unique=False)
    omschrijving = models.CharField(max_length=256, null=False, blank=False)
    bedrijf = models.ForeignKey(Bedrijf, null=False, blank=False, on_delete=models.CASCADE)
    opdrachtgever = models.ForeignKey(Contactpersoon, blank=True, null=True, on_delete=models.CASCADE)
    orderstadium = models.ForeignKey(Orderstadium, related_name='Order_Stadium', null=False, blank=False, on_delete=models.CASCADE)
    geschatte_omzet = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    werkelijke_omzet = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    einddatum_project = models.DateField()
    broncampagne = models.CharField(max_length=80, blank=True, null=True)
    onenote_doc = models.URLField(blank=True, null=True)
    klantpartner = models.ForeignKey(User, related_name='Order_Klantpartner', blank=True, null=True, on_delete=models.CASCADE)
    actief = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Orders'

    def __unicode__(self):
        return self.projectcode    