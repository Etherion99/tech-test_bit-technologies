from django.db import models


class PropertyType(models.Model):
    name = models.CharField(max_length=50, unique=True)

    def __str__(self) -> str:
        return str(self.name)


class Property(models.Model):
    name = models.CharField(max_length=200)
    type = models.ForeignKey(PropertyType, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    area = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return str(self.name)
