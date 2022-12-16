from django.db import models
from product.models import Product


# Create your models here.
class Strategy(models.Model):
    title = models.CharField(max_length=300)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, blank=True, null=True, related_name='strategy_product')

    def __str__(self) -> str:
        return self.title + ' ' + str(self.product.full_title)


# todo Додумать модельку элемента стратегии
class StrategyElement(models.Model):
    PLUS = '+'
    EQUATION = '='
    MINUS = '-'
    MULTIPLY = '*'
    DIVIDE = '/'
    BASIC_OPERATIONS = [
        (PLUS, '+'),
        (EQUATION, '='),
        (MINUS, '-'),
        (MULTIPLY, '*'),
        (DIVIDE, '/'),
    ]
    title = models.CharField(max_length=300)
    operation = models.CharField(max_length=300, choices=BASIC_OPERATIONS, default=EQUATION, blank=True, null=True)
    custom_value = models.PositiveIntegerField(blank=True, null=True)
    strategy = models.ForeignKey(Strategy, on_delete=models.SET_NULL, blank=True, null=True, related_name='strategyelemnt_strategy')
    

    @property
    def median_prices_competitors(self):
        pass

    @property
    def most_popular_price_competitors(self):
        pass

    @property
    def quantity_competitors(self):
        pass

    @property
    def quantity_competitors_with_prices(self):
        pass

    @property
    def quantity_competitors_with_product_in(self):
        pass

    @property
    def quantity_competitors_with_prices_product_in(self):
        pass

    @property
    def min_price_competitors(self):
        pass

    @property
    def average_price_competitors(self):
        pass

    @property
    def max_price_competitors(self):
        pass
