from django.db import models


class Product(models.Model):
    RING = "Ring"
    NECKLACE = "Necklace"
    CHAIN = "Chain"
    EARRINGS = "Earrings"
    # IMAGE_UPLOAD_TO_DIR = 'products/'

    TYPES = [(x, x) for x in (RING, NECKLACE, CHAIN, EARRINGS)]
    PRODUCT_NAME_MAX_LEN = 30

    name = models.CharField(
        max_length=PRODUCT_NAME_MAX_LEN,
        # null=False,
        # blank=False,
    )

    type = models.CharField(
        max_length=max(len(x) for (x, _) in TYPES),
        choices=TYPES,
    )

    description = models.TextField(
        null=True,
        blank=True,
    )

    image = models.ImageField(
        # upload_to=IMAGE_UPLOAD_TO_DIR,
        null=True,
        blank=True,
        default='no_image.png'
    )

    price = models.FloatField(
        null=False,
        blank=False,
    )

    def __str__(self):
        return f'{self.type}'
