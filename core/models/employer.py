from django.db import models
from core.models import Company

class Employer(models.Model):
    name = models.CharField(max_length=255)
    position = models.CharField(max_length=255)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, related_name='employers')
    entry_date = models.CharField(max_length=10, null=True, blank=True)
    exit_date = models.CharField(max_length=10, null=True, blank=True)
    vacation_date = models.CharField(max_length=10, null=True, blank=True)

    def __str__(self):
        return (self.name, self.position)