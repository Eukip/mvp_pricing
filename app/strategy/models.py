from decimal import Decimal
from django.db import models
from django.db.models import Max, Min, Avg
from users.models import User


# Create your models here.
class Strategy(models.Model):
    title = models.CharField(max_length=300)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, blank=True, null=True, related_name='strategy_user')

    def __str__(self) -> str:
        return self.title + ' ' + str(self.product.full_title)


class StrategyElementVariable(models.Model):
    MEDIAN_PRICES_C = 'медианная цена конкурентов'
    MIN_PRICE_C = 'минимальная цена конкурентов'
    AVERAGE_PRICE_C = 'средняя цена конкурентов'
    MAX_PRICE_C = 'максимальная цена конкурентов'
    BASIC_VARIABLES = [
        (MEDIAN_PRICES_C, 'медианная цена конкурентов'),
        (MIN_PRICE_C, 'минимальная цена конкурентов'),
        (AVERAGE_PRICE_C, 'средняя цена конкурентов'),
        (MAX_PRICE_C, 'максимальная цена конкурентов'),
    ]
    title = models.CharField(max_length=300, choices=BASIC_VARIABLES, blank=True, null=True)
    custom_variable = models.IntegerField(blank=True, null=True)
    strategy = models.ForeignKey(Strategy, on_delete=models.SET_NULL, blank=True, null=True)

    # todo need to test properties
    @property
    def competitors_product_query(self):
        from product.models import CompetitorProduct
        queryset = CompetitorProduct.objects.exclude(competitor=self.strategy.product_strategy.creator)
        return queryset

    @property
    def median_prices_competitors(self): 
        queryset = self.competitors_product_query
        count_competitors_product = queryset.count()
        values = queryset.product.values_list('current_price_before_discount', flat=True).order_by('current_price_before_discount')
        if count_competitors_product % 2 == 1:
            return values[int(round(count_competitors_product/2))]
        else:
            return sum(values[count_competitors_product/2-1:count_competitors_product/2+1])/Decimal(2.0)

    @property
    def min_price_competitors(self):
        queryset = self.competitors_product_query
        return queryset.product.aggregate(Min('current_price_before_discount'))

    @property
    def average_price_competitors(self):
        queryset = self.competitors_product_query
        return queryset.product.aggregate(Avg('current_price_before_discount'))

    @property
    def max_price_competitors(self):
        queryset = self.competitors_product_query
        return queryset.product.aggregate(Max('current_price_before_discount'))

    @property
    def price_after_all_discounts(self):
        return self.strategy.product_strategy


class StrategyLogicOperation(models.Model):
    LESS = '<'
    EQUAL = '=='
    GREATER = '>'
    NOTEQUAL = '!='
    LESSOREQUAL = '<='
    GREATEROREQUAL = '>='
    BASIC_OPERATIONS = [
        (LESS, '<'),
        (EQUAL, '=='),
        (GREATER, '>'),
        (NOTEQUAL, '!='),
        (LESSOREQUAL, '<='),  
        (GREATEROREQUAL, '>=')
    ]

    TRUE = True
    FALSE = False
    BASIC_RESULTS = [
        (TRUE, True),
        (FALSE, False)
    ]

    operation = models.CharField(max_length=2, choices=BASIC_OPERATIONS, default=EQUAL, blank=True, null=True)
    first_variable = models.ForeignKey(StrategyElementVariable, on_delete=models.SET_NULL, blank=True, null=True, related_name='first_logic_variable')
    second_variable = models.ForeignKey(StrategyElementVariable, on_delete=models.SET_NULL, blank=True, null=True, related_name='second_logic_variable')
    result = models.BooleanField(choices=BASIC_RESULTS, blank=True, null=True, default=TRUE)
    parent_logical_operation = models.ForeignKey('StrategyLogicOperation', on_delete=models.SET_NULL, blank=True, null=True, related_name='nested_logical_operation')


class IfLogicOperation(models.Model):
    result = models.BooleanField(default=True)

class StrategyOperation(models.Model):
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
    operation = models.CharField(max_length=300, choices=BASIC_OPERATIONS, default=EQUATION, blank=True, null=True)
    custom_value = models.PositiveIntegerField(blank=True, null=True)
    variable = models.ForeignKey(StrategyElementVariable, on_delete=models.SET_NULL, null=True, blank=True, related_name='operation_variable')
    strategy = models.ForeignKey(Strategy, on_delete=models.SET_NULL, blank=True, null=True, related_name='strategyoperation_strategy')
    logic_result = models.ForeignKey(StrategyLogicOperation,
                                    on_delete=models.CASCADE, blank=True, null=True, related_name='operation_result')

    def __str__(self) -> str:
        return 'Операция' + str(self.id) + 'стратегии' + str(self.strategy.id)
