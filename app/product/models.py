from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)


class SubCategory(models.Model):
    title = models.CharField(max_length=300)
    related_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)


class SubSubCategory(models.Model):
    title = models.CharField(max_length=300)
    related_sub_categoy = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)


class RoleProduct(models.Model):
    title = models.CharField(max_length=300)


class Product(models.Model):
    full_title = models.CharField(max_length=300)
    vendor_code = models.CharField(max_length=300, blank=True, null=True)
    article = models.CharField(max_length=300, blank=True, null=True)
    # url_product
    # todo: наследование и ссылки конкурента как-то отделить
    purchase_price = models.PositiveIntegerField(blank=True, null=True)
    price_before_discount = models.PositiveIntegerField(blank=True, null=True)
    price_after_dicount = models.PositiveIntegerField(blank=True, null=True)
    promotional_price = models.PositiveIntegerField(blank=True, null=True)
    standart_price = models.PositiveIntegerField(blank=True, null=True)
    max_price = models.PositiveIntegerField(blank=True, null=True)
    min_price = models.PositiveIntegerField(blank=True, null=True)
    rrc_price = models.PositiveIntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=300, blank=True, null=True)
    brand = models.CharField(max_length=300, blank=True, null=True)
    create_date = models.DateField(auto_now_add=True)
    role = models.ForeignKey(RoleProduct, on_delete=models.CASCADE, blank=True, null=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    # id_strategy = models.ForeignKey(Strategy, on_delete=models.CASCADE, blank=True, null=True)
    # competitors = models.ForeignKey()
    # остаток склад регион
    # аналог товаров ссылки