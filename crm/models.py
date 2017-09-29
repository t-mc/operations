from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

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
                                           blank=True
                                           )

    class Meta:
        abstract = True


# Create your models here.

class Branche(TransactionDT):
    branch = models.CharField(max_length=80, unique=True)

    class Meta:
        verbose_name_plural = 'Branches'

    def __str__(self):
        return self.branch


class Adres(TransactionDT):
    ADRESTYPE_CHOICES = (
        ('P', 'Postadres'),
        ('B', 'Bezoekadres')
    )

    adrestype = models.CharField(max_length=1, choices=ADRESTYPE_CHOICES, null=False, blank=False)
    adresregel_1 = models.CharField(max_length=80, null=True)
    adresregel_2 = models.CharField(max_length=80, blank=True, null=True)
    postcode = models.CharField(max_length=7, null=True)
    plaats = models.CharField(max_length=80, null=True)
    Land = models.CharField(max_length=80, null=True)

    class Meta:
        verbose_name_plural = 'Adressen'

    def __str__(self):
        return self.adresregel_1 + ', ' + self.postcode + ' ' + self.plaats



class Bedrijf(TransactionDT):
    bedrijfsnaam = models.CharField(max_length=120, unique=True)
    telefoonnummer = PhoneNumberField(blank=True, null=True)
    branche = models.ForeignKey(Branche, blank=True, null=True)
    email = models.EmailField(max_length=75, blank=True, null=True)
    website = models.URLField(max_length=200, blank=True, null=True)
    kvk_nummer = models.CharField(max_length=20, blank=True, null=True)
    onenote = models.URLField(max_length=400, blank=True, null=True)
    actief = models.BooleanField(default=True)
    klantpartner = models.ForeignKey(User, related_name='Klantpartner', blank=True, null=True)
    adres = models.ForeignKey(Adres, blank=True, null=True)

    class Meta:
        ordering = ['bedrijfsnaam']
        verbose_name_plural = 'Bedrijven'

    def __str__(self):
        return self.bedrijfsnaam

      
class Contactpersoon(TransactionDT):
    GENDER_CHOICES = (
        ('M', 'Man'),
        ('V', 'Vrouw'),
        ('O', 'Onbekend')
    )

    volledige_naam = models.CharField(max_length=120)
    initialen = models.CharField(max_length=20)
    voornaam = models.CharField(max_length=120)
    tussenvoegsel = models.CharField(max_length=120, blank=True, null=True)
    achternaam = models.CharField(max_length=120)
    telefoonnummer = PhoneNumberField(blank=True, null=True)
    mobielnummer = PhoneNumberField(blank=True, null=True)
    email = models.EmailField(max_length=75, null=True)
    bedrijf = models.ForeignKey(Bedrijf, blank=True, null=True)
    standplaats = models.ForeignKey(Adres, blank=True, null=True)
    functie = models.CharField(max_length=120, blank=True, null=True)
    afdeling = models.CharField(max_length=120, blank=True, null=True)
    assistent = models.CharField(max_length=120, blank=True, null=True)
    manager = models.CharField(max_length=120, blank=True, null=True)
    overige_contactgegevens = models.CharField(max_length=120, blank=True, null=True)
    actief = models.BooleanField(default=True)
    sexe = models.CharField('geslacht', max_length=1, choices=GENDER_CHOICES, default='O', null=False, blank=False)

    class Meta:
        ordering = ['volledige_naam']
        verbose_name_plural = 'Contactpersonen'

    def __str__(self):
        return self.volledige_naam
    