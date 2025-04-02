from django.db import models

# Create your models here.
class anamnesis (models.Model):
    weight = models.IntegerField();
    age = models.IntegerField();
    vaccination = models.BooleanField();
    observation = models.TextField();
    
    def __str__(self): self.name