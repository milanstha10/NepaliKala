from django.db import models

class Category(models.TextChoices):
    RINGS = "Rings", "Rings"
    NECKLACES = "Necklaces", "Necklaces"
    BRACELETS = "Bracelets", "Bracelets"
    EARRINGS = "Earrings", "Earrings"


class Product(models.Model):
    name = models.CharField(max_length=255)

    price = models.DecimalField(
        max_digits=10,
        decimal_places=2
    )

    description = models.TextField()

    stock = models.BooleanField(default=True)

    image = models.ImageField(
        upload_to="products/",
        blank=True,
        null=True
    )

    size = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    material = models.CharField(
        max_length=100,
        blank=True,
        null=True
    )

    category = models.CharField(
        max_length=20,
        choices=Category.choices,
        default=Category.RINGS
    )

    def __str__(self):
        return self.name
