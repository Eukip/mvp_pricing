from django.db import models

# Create your models here.
class Strategy(models.Model):
    title = models.CharField(max_length=300)


class StrategyElement(models.Model):
    title = models.CharField(max_length=300)
    operation = models.CharField(max_length=300)
    # variable = 