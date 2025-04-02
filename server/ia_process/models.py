from django.db import models


class review(models.Model):
    name = models.CharField(max_length = 100);
    anamnesis = models.TextField(max_length = 1000);

