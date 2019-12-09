from django.db import models, IntegrityError
from django.conf import settings
from datetime import date
import random
import string
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

from crm.models import Bedrijf, Contactpersoon
from projecten.models import Verkoopkans
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

#
# Lookup tabel voor case status
#
class CaseStatus(models.Model):
    status = models.CharField(max_length=48, unique=True)

    class Meta:
        verbose_name_plural = 'Case statussen'

    def __unicode__(self):
        return self.status

    def __str__(self):
        return self.status    

#
# Lookup tabel voor activiteit status
#
class ActivityStatus(models.Model):
    status = models.CharField(max_length=48, unique=True)

    class Meta:
        verbose_name_plural = 'Activiteit statussen'
        verbose_name = 'Activiteit status'

    def __unicode__(self):
        return self.status

    def __str__(self):
        return self.status 
#
# Lookup tabel voor case typen
#
class CaseType(models.Model):
    case_type = models.CharField(max_length=48)

    class Meta:
        verbose_name_plural = 'Case typen'

    def __unicode__(self):
        return self.case_type

    def __str__(self):
        return self.case_type 
#
# Lookup tabel voor activiteit soorten
#
class ActivityType(models.Model):
    activiteit_type = models.CharField(max_length=48, unique=True)

    class Meta:
        verbose_name_plural = 'Activiteit typen'
        verbose_name = 'Activiteit type'

    def __unicode__(self):
        return self.activiteit_type

    def __str__(self):
        return self.activiteit_type 
#
# Lookup tabel voor tijdsduur
#
class Tijdsduur(models.Model):
    minuten = models.DurationField(blank=True, null=True)

    class Meta:
        verbose_name_plural = 'Tijdsduur'
        ordering = ['minuten']

    def __unicode__(self):
        return str(self.minuten)

    def __str__(self):
        return str(self.minuten)

#
# Record layout contracten tabel
#
class Contract(TransactionDT):
    projectcode = models.ForeignKey(Verkoopkans, blank=True, null=True, on_delete=models.CASCADE)
    bedrijf = models.ForeignKey(Bedrijf, related_name='Contractbij_Klant', blank=True, null=True, on_delete=models.CASCADE)
    startdatum = models.DateField()
    einddatum = models.DateField()
    klantpartner = models.ForeignKey(User, verbose_name="Contracteigenaar", related_name='Contract_Klantpartner', blank=True, null=True, on_delete=models.CASCADE)
    contract_bij = models.ForeignKey(Bedrijf, related_name='Contractbij_Leverancier', blank=True, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Contracten'

    def __unicode__(self):
        return str(self.projectcode)

    def __str__(self):
        return str(self.projectcode) 

#
# Record layout cases tabel
#
class Cases(TransactionDT):
    case_code = models.CharField(max_length=16, blank=True, unique=True)
    case_type = models.ForeignKey(CaseType, null=True, default=1, on_delete=models.CASCADE)
    onderwerp = models.CharField(max_length=64)
    omschrijving = models.TextField()
    datum_melding = models.DateField(("Datum melding"), default=date.today)
    datum_gereed = models.DateField(("Datum gereed"), blank=True, null=True)
    status = models.ForeignKey(CaseStatus, null=True, default=1, on_delete=models.CASCADE)
    bedrijf = models.ForeignKey(Bedrijf, blank=True, null=True, on_delete=models.CASCADE)
    contact = models.ForeignKey(Contactpersoon, blank=True, null=True, on_delete=models.CASCADE)
    contract = models.ForeignKey(Contract, blank=True, null=True, on_delete=models.CASCADE)
    uitvoerende = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='user_uitvoerende', on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Cases'
        verbose_name = 'Case'

    def __unicode__(self):
        return self.case_code

    def __str__(self):
        return self.case_code

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
class Activiteiten(TransactionDT):
    case_id = models.ForeignKey(Cases, on_delete=models.CASCADE)
    activiteit = models.ForeignKey(ActivityType, on_delete=models.CASCADE)
    status = models.ForeignKey(ActivityStatus, on_delete=models.CASCADE)
    omschrijving = models.TextField()
    uitvoerende = models.ForeignKey(settings.AUTH_USER_MODEL, default=1, related_name='act_uitvoerende', on_delete=models.CASCADE)
    datum_uitgevoerd = models.DateField(("Datum"), default=date.today)
    tijdsduur = models.ForeignKey(Tijdsduur, blank=True, null=True, default=1, on_delete=models.CASCADE)

    class Meta:
        verbose_name_plural = 'Activiteiten'
        verbose_name = 'Activiteit'

    def __unicode__(self):
        return str(self.case_id)

    def __str__(self):
        return str(self.case_id) 
#
# Functie voor het genereren van alfanumerieke case code
#
def id_generator(size=8, chars=string.ascii_uppercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

