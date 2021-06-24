from django.db import models

# Create your models here.
class product(models.Model):
    """Model definition for product."""

    # TODO: Define fields here

    class Meta:
        """Meta definition for product."""

        verbose_name = 'product'
        verbose_name_plural = 'products'

    def __str__(self):
        """Unicode representation of product."""
        pass
