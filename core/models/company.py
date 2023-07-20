from django.db import models

class Company(models.Model):
    name = models.CharField(max_length=255)
    site = models.URLField()
    
    def __str__(self):
        return self.name