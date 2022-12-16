from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()


# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title

class SubCategory(models.Model):
    title = models.CharField(max_length=300)
    related_category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title + ' '+ str(self.related_category.title)


class SubSubCategory(models.Model):
    title = models.CharField(max_length=300)
    related_sub_categoy = models.ForeignKey(SubCategory, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self) -> str:
        return self.title + ' ' + str(self.related_sub_categoy.title)


class RoleProduct(models.Model):
    title = models.CharField(max_length=300)

    def __str__(self) -> str:
        return self.title


class Product(models.Model):
    thing = models.CharField(max_length=300)
    vendor_code = models.CharField(max_length=300, blank=True, null=True)
    article_provider = models.CharField(max_length=300, blank=True, null=True)
    nomenclature_1c_code = models.IntegerField(blank=True, null=True)
    last_barcode = models.IntegerField(blank=True, null=True)
    url_product = models.URLField(blank=True, null=True)
    # todo: наследование и ссылки конкурента как-то отделить
    purchase_price = models.PositiveIntegerField(blank=True, null=True)
    current_price_before_discount = models.PositiveIntegerField(blank=True, null=True)
    new_price_before_discount = models.PositiveIntegerField(blank=True, null=True)
    price_after_dicount = models.PositiveIntegerField(blank=True, null=True)
    current_discount = models.PositiveIntegerField(blank=True, null=True)
    recommended_discount = models.PositiveIntegerField(blank=True, null=True)
    agreed_discount = models.PositiveIntegerField(blank=True, null=True)
    cuurent_discount_promo = models.PositiveIntegerField(blank=True, null=True)
    new_discount_promo = models.PositiveIntegerField(blank=True, null=True)
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
    remainder = models.PositiveIntegerField(blank=True, null=True)
    storage = models.CharField(max_length=300, blank=True, null=True)
    region = models.CharField(max_length=300, blank=True, null=True)

    @property
    def full_title(self):
        return self.thing + ' ' + self.title + ' ' + self.brand

    def __str__(self) -> str:
        return self.full_title
