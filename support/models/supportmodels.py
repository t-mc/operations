from django.db import models, IntegrityError
from django.conf import settings
from datetime import date
import random
import string
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

#
# Lookup tabel voor case status
#
class CaseStatus(models.Model):
    status = models.CharField(max_length=24, unique=True)

    class Meta:
        verbose_name_plural = 'Case statussen'

    def __str__(self):
        return self.status

#
# Lookup tabel voor activiteit status
#
class ActivityStatus(models.Model):
    status = models.CharField(max_length=24, unique=True)

    class Meta:
        verbose_name_plural = 'Activiteit statussen'

    def __str__(self):
        return self.status

#
# Lookup tabel voor case typen
#
class CaseType(models.Model):
    type = models.CharField(max_length=24)

    class Meta:
        verbose_name_plural = 'Case typen'

    def __str__(self):
        return self.type

#
# Lookup tabel voor activiteit soorten
#
class ActivityType(models.Model):
    type = models.CharField(max_length=24, unique=True)

    class Meta:
        verbose_name_plural = 'Activiteit typen'

    def __str__(self):
        return self.type

#
# Record layout bedrijven tabel
#
class Bedrijf(models.Model):
    bedrijfsnaam = models.CharField(max_length=64)
    telefoon = PhoneNumberField(blank=True, null=True)
    telefoonnummer = models.CharField(max_length=20)
    primair_contact = models.CharField(max_length=64)
    klantpartner = models.CharField(max_length=254)
    emailadres = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Bedrijven'

    def __str__(self):
        return self.bedrijfsnaam

#
# Record layout contactpersonen tabel
#
class Contactpersoon(models.Model):
    contactnaam = models.CharField(max_length=64)
    functie = models.CharField(max_length=64)
    telefoonnummer = models.CharField(max_length=20)
    mobielnummer = models.CharField(max_length=20)
    emailadres = models.CharField(max_length=254)
    bedrijf = models.ForeignKey(Bedrijf, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Contactpersonen'

    def __str__(self):
        return self.contactnaam

#
# Record layout leverancier tabel
#
class Leverancier(models.Model):
    leveranciernaam = models.CharField(max_length=64)
    telefoonnummer = models.CharField(max_length=20)
    emailadres = models.CharField(max_length=254)
    klantpartner = models.CharField(max_length=254)

    class Meta:
        verbose_name_plural = 'Leveranciers'

    def __str__(self):
        return self.leveranciernaam

#
# Record layout contracten tabel
#
class Contract(models.Model):
    projectcode = models.CharField(max_length=6)
    bedrijf = models.ForeignKey(Bedrijf, blank=True, null=True)
    startdatum = models.DateField()
    einddatum = models.DateField()
    klantpartner = models.CharField(max_length=254)
    contract_bij = models.ForeignKey(Leverancier, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Contracten'

    def __str__(self):
        return self.projectcode

#
# Record layout sla tabel
#
class SLA(models.Model):
    omschrijving = models.CharField(max_length=64)
    classificatie = models.CharField(max_length=20)
    bevestiging = models.IntegerField()
    oplossingsplan = models.IntegerField()
    workaround = models.IntegerField()
    oplossing = models.IntegerField()
    leverancier = models.ForeignKey(Leverancier, blank=True, null=True)

    class Meta:
        verbose_name_plural = 'SLA-s'

    def __str__(self):
        return self.classificatie

#
# Record layout cases tabel
#
class Cases(models.Model):
    case_code = models.CharField(max_length=16, editable=False, unique=True)
    onderwerp = models.CharField(max_length=64)
    omschrijving = models.TextField()
    datum_melding = models.DateField(("Datum melding"), default=date.today)
    datum_gereed = models.DateField(("Datum gereed"), blank=True, null=True)
    status = models.ForeignKey(CaseStatus, null=True)
    bedrijf = models.ForeignKey(Bedrijf, blank=True, null=True)
    contact = models.ForeignKey(Contactpersoon, blank=True, null=True)
    contract = models.ForeignKey(Contract, blank=True, null=True)
    uitvoerende = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)

    class Meta:
        verbose_name_plural = 'Cases'

    def __str__(self):
        return self.onderwerp

    def save(self, *args, **kwargs):
        if not self.case_code:
            self.case_code = id_generator()
            # using your function as above or anything else
        success = False
        failures = 0
        while not success:
            try:
                super(Cases, self).save(*args, **kwargs)
            except IntegrityError:
                 failures += 1
                 if failures > 5: # or some other arbitrary cutoff point at which things are clearly wrong
                     raise
                 else:
                     # looks like a collision, try another random value
                     self.auto_pseudoid = id_generator()
            else:
                 success = True

#
# Record layout voor activiteiten tabel
#
class Activiteiten(models.Model):
    case_id = models.ForeignKey(Cases)
    activiteit = models.ForeignKey(ActivityType)
    status = models.ForeignKey(ActivityStatus)
    omschrijving = models.TextField()
    uitvoerende = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    datum_uitgevoerd = models.DateField(("Datum"), default=date.today)

    class Meta:
        verbose_name_plural = 'Activiteiten'

    # def __str__(self):
    #     return self.activiteit

#
# Functie voor het genereren van alfanumerieke case code
#
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

