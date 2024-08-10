from django.db import models

from django.db import models

class Image(models.Model):
    name = models.CharField(max_length=255)
    image_data = models.BinaryField()

    def __str__(self):
        return self.name
