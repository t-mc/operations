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
    last_modified_user = models.ForeignKey(
        "auth.User",
        verbose_name="Laatst gewijzigd door",
        null=True,
        blank=True,
        on_delete=models.CASCADE,
    )

    class Meta:
        abstract = True


class Productgroep(TransactionDT):
    productcode = models.CharField(max_length=10, unique=True)
    omschrijving = models.CharField(max_length=80, unique=True)
    productowner = models.ForeignKey(
        User,
        related_name="productowner",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
        limit_choices_to={"is_active": True},
    )
    leverancier = models.ForeignKey(
        Bedrijf, null=False, blank=False, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["productcode"]
        verbose_name_plural = "Productgroepen"

    def __str__(self):
        return self.omschrijving


EENHEID_KEUZE = (("S", "Stuksprijs"), ("U", "Uurprijs"), ("D", "Dagprijs"))


class Product(models.Model):
    code = models.CharField(max_length=15, null=False, blank=False, unique=True)
    omschrijving = models.CharField(max_length=80, null=False, blank=False, unique=True)
    productgroep = models.ForeignKey(
        "Productgroep", null=False, blank=False, on_delete=models.CASCADE
    )
    prijs_per_eenheid = models.DecimalField(
        max_digits=12, decimal_places=2, blank=True, null=True
    )
    eenheid = models.CharField(
        max_length=1, null=False, blank=False, choices=EENHEID_KEUZE
    )

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Producten"

    def __str__(self):
        return "%s per %s" % (self.code, self.get_eenheid_display())


class Training(TransactionDT):
    omschrijving = models.CharField(max_length=80, unique=True)
    productgroep = models.ForeignKey(
        Productgroep, null=False, blank=False, on_delete=models.CASCADE
    )

    class Meta:
        ordering = ["omschrijving"]
        verbose_name_plural = "Trainingen"

    def __str__(self):
        return self.omschrijving


class Marketinguiting(TransactionDT):
    omschrijving = models.CharField(max_length=80, unique=True)

    class Meta:
        ordering = ["omschrijving"]
        verbose_name_plural = "Marketinguitingen"

    def __str__(self):
        return self.omschrijving
