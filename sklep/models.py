from django.db import models

# Create your models here.

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    vat = models.DecimalField(max_digits=2, decimal_places=2)
    valid_to = models.DateField(blank=True, null=True)
    available = models.BooleanField(default=True)

    def vat_jako_calkowita(self):
        return int(100 * self.vat)

