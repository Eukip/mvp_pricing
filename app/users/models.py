from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin
from django.utils import timezone
from .manager import UserManager
from product.models import Product


# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField('email address', unique=True)
    first_name = models.CharField('first name', max_length=100)
    last_name = models.CharField('last name', max_length=100)

    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    date_created = models.DateTimeField(default=timezone.now)


    USERNAME_FIELD = 'email'

    REQUIRED_FIELDS = []

    objects = UserManager()

    def __str__(self):
        return self.email


class Competitor(models.Model):
    title = models.CharField(max_length=300, blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, related_name='competitor_product')

    def __str__(self) -> str:
        return self.title + self.product.title


class AnalogProduct(models.Model):
    title = models.CharField(max_length=300)
    article = models.CharField(max_length=300, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True, blank=True, related_name='analogproduct_product')
    competitor = models.ForeignKey(Competitor, on_delete=models.SET_NULL, blank=True, null=True, related_name='analogproduct_competitor')

    def __str__(self) -> str:
        return 'Аналог' + self.id + " " + self.product.title
