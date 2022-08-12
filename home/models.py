import email
from django.db import models
class Emp(models.Model):
    name=models.CharField(max_length=20)
    email=models.EmailField(max_length=40)
    mob=models.IntegerField()
    def __str__(self) -> str:
        return self.name
