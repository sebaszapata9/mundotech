from django.db import models


# Create your models here.
class Phone(models.Model):
    name = models.CharField(max_length=100)
    brand = models.CharField(max_length=50)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    release_date = models.DateField()
    specs = models.TextField()
    new_release = models.BooleanField(default=False)

    def __str__(self):
        return self.name