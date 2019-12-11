# from django.utils.functional import cached_property
import decimal

from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import Sum
from django.utils.html import format_html

from crm.models import Bedrijf, Contactpersoon
from producten.models import Productgroep, Product, Training


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
    opdrachtgever = models.ForeignKey(Contactpersoon, related_name='Verkoopkans_Opdrachtgever', blank=True, null=True, on_delete=models.CASCADE)
    kwo_ontvanger = models.ForeignKey(Contactpersoon, related_name='Verkoopkans_KWO_Ontvanger', blank=True, null=True, on_delete=models.CASCADE)
    verkoopstadium = models.ForeignKey(Verkoopstadium, related_name='Verkoop_Stadium', null=False, blank=False, on_delete=models.CASCADE)
    geschatte_omzet = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    werkelijke_omzet = models.DecimalField(max_digits=12, decimal_places=2, blank=True, null=True)
    startdatum_project = models.DateField(blank=True, null=True)
    einddatum_project = models.DateField(blank=True, null=True)
    onenote_doc = models.URLField(blank=True, null=True)
    klantpartner = models.ForeignKey(User, verbose_name="Leadeigenaar", related_name='Verkoopkans_Klantpartner', blank=True, null=True, on_delete=models.CASCADE)
    ordereigenaar = models.ForeignKey(User, related_name='Verkoopkans_Ordereigenaar', blank=True, null=True, on_delete=models.CASCADE)
    productgroep = models.ForeignKey(Productgroep, related_name='Verkoopkans_Productgroep', blank=True, null=True, on_delete=models.CASCADE)
    actief = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Verkoopkansen'
        ordering = ['projectcode']

    # @cached_property
    def totaal_omzet(self):
        telling = Omzetpermaand.objects.filter(projectcode__projectcode=self.projectcode).aggregate(bedrag = Sum('omzet'))
        if telling['bedrag'] != None:
            # return telling['bedrag']
            resultaat = telling['bedrag']
            return format_html('%s' % (resultaat))
        else: 
            return decimal.Decimal(0.00).quantize(decimal.Decimal('0.00'))

    def __unicode__(self):
        return self.projectcode    

    def __str__(self):
        return self.projectcode    


MAAND_KEUZE = (
    (1, 'Januari'),
    (2, 'Februari'),
    (3, 'Maart'),
    (4, 'April'),
    (5, 'Mei'),
    (6, 'Juni'),
    (7, 'Juli'),
    (8, 'Augustus'),
    (9, 'September'),
    (10, 'Oktober'),
    (11, 'November'),
    (12, 'December'),
)
JAAR_KEUZE = (
    (1, '2018'),
    (2, '2019'),
    (3, '2020'),
    (4, '2021'),
    (5, '2022'),
    (6, '2023'),
    (7, '2024'),
    (8, '2025'),
    (9, '2026'),
    (10, '2027'),
)
class Omzetpermaand(TransactionDT):
    projectcode = models.ForeignKey(Verkoopkans, related_name='Omzetpermaand_Verkoopkans', on_delete=models.CASCADE)    
    jaar = models.IntegerField(null=False, blank=False, choices=JAAR_KEUZE)
    maand = models.IntegerField(null=False, blank=False, choices=MAAND_KEUZE)
    omzet = models.DecimalField('Omzet in euro\'s', max_digits=10, decimal_places=2)

    class Meta:
        verbose_name_plural = 'Omzetten per maand'
        ordering = ['jaar', 'maand']
        unique_together = ('projectcode', 'jaar', 'maand')

    def __unicode__(self):
        for loop in JAAR_KEUZE:
            if loop[0] == self.jaar:
                jaar = loop[1]
        for loop in MAAND_KEUZE:
            if loop[0] == self.maand:
                maand = loop[1]
        return '%s - %s - %s' % (self.projectcode, jaar, maand)   

    def __str__(self):
        for loop in JAAR_KEUZE:
            if loop[0] == self.jaar:
                jaar = loop[1]
        for loop in MAAND_KEUZE:
            if loop[0] == self.maand:
                maand = loop[1]
        return '%s - %s - %s' % (self.projectcode, jaar, maand)   

class Orderregel(TransactionDT):
    projectcode = models.ForeignKey(Verkoopkans, related_name='Orderregel_Verkoopkans', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    aantal_eenheden = models.IntegerField('Aantal Eenheden' ,null=False, blank=False)
    list_prijs = models.DecimalField('Listprijs per eenheid', max_digits=12, decimal_places=2, blank=True, null=True)
    selling_prijs = models.DecimalField('Sellingprijs per eenheid', max_digits=12, decimal_places=2, blank=True, null=True)
    regel_totaal_prijs = models.DecimalField('Regel totaalprijs', max_digits=14, decimal_places=2, blank=True, null=True)

    class Meta:
        verbose_name = "Orderregel"
        verbose_name_plural = "Orderregels"

    def __str__(self):
        return '%s - %s' % (self.projectcode, self.product)

class Orders(Verkoopkans):
    class Meta:
        verbose_name_plural = 'Orders'
        proxy = True

class Order(TransactionDT):
    
    projectcode = models.CharField(max_length=10, unique=False)
    omschrijving = models.CharField(max_length=256, null=False, blank=False)
    bedrijf = models.ForeignKey(Bedrijf, null=False, blank=False, on_delete=models.CASCADE)
    opdrachtgever = models.ForeignKey(Contactpersoon, related_name='Order_Opdrachtgever', blank=True, null=True, on_delete=models.CASCADE)
    kwo_ontvanger = models.ForeignKey(Contactpersoon, related_name='Order_KWO_Ontvanger', blank=True, null=True, on_delete=models.CASCADE)
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

    def __str__(self):
        return self.projectcode    


class Trainingregistratie(TransactionDT):
    contactpersoon = models.ForeignKey(Contactpersoon, blank=False, null=False, on_delete=models.CASCADE)
    training = models.ForeignKey(Training, blank=False, null=False, on_delete=models.CASCADE)
    order = models.ForeignKey(Verkoopkans, blank=False, null=False, on_delete=models.CASCADE)
    trainer = models.ForeignKey(User, related_name='Trainer', blank=False, null=False, on_delete=models.CASCADE)
    bijzonderheden = models.CharField(max_length=512, blank=True, null=True)
    datum = models.DateField(blank=False, null=False)

    class Meta:
        ordering = ['training', 'order']
        verbose_name_plural = 'Trainingsregistraties'

    def __unicode__(self):
        return self.training.omschrijving + ', ' + self.order.projectcode + ', ' + str(self.datum) + ', ' + self.trainer.username

    def __str__(self):
        return self.training.omschrijving + ', ' + self.order.projectcode + ', ' + str(self.datum) + ', ' + self.trainer.username


class Urenpermedewerker(TransactionDT):
    projectcode = models.ForeignKey(Verkoopkans, related_name='Urenpermedewerker_Order', on_delete=models.CASCADE)    
    medewerker = models.ForeignKey(User, related_name='Medewerker_Order', blank=True, null=True, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, related_name='Medewerker_Order_Product', blank=True, null=True, on_delete=models.CASCADE)
    jaar = models.IntegerField(null=False, blank=False, choices=JAAR_KEUZE)
    maand = models.IntegerField(null=False, blank=False, choices=MAAND_KEUZE)
    uren = models.PositiveSmallIntegerField(null=False, blank=False)    

    class Meta:
        verbose_name_plural = 'Uren per medewerker'
        ordering = ['medewerker', 'jaar', 'maand']
        unique_together = ('medewerker', 'projectcode', 'jaar', 'maand')

    def __unicode__(self):
        for loop in JAAR_KEUZE:
            if loop[0] == self.jaar:
                jaar = loop[1]
        return '%s - %s - %s - %s' % (self.projectcode, self.medewerker.username, jaar, self.maand)

    def __str__(self):
        for loop in JAAR_KEUZE:
            if loop[0] == self.jaar:
                jaar = loop[1]
        return '%s - %s - %s - %s' % (self.projectcode, self.medewerker.username, jaar, self.maand)