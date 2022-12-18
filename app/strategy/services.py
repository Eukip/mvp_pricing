from django.db.models import Max, Min, Avg
from decimal import Decimal


class StrategyOperator():
    
    def __init__(self, current_price_before_discount, variable) -> None:
        self.target_strategy = current_price_before_discount
        self.variable = variable

    def plus(self) -> int:
        return self.target_strategy + self.variable
    
    def minus(self) -> int:
        return self.target_strategy - self.variable
    
    def quation(self) -> int:
        return self.variable

    def multiply(self) -> int:
        return self.target_strategy * self.variable
    
    def divide(self) -> int:
        return self.target_strategy / self.variable


class StrategyLogicOperator():

    def __init__(self, first_variable, second_variable) -> None:
        self.first_variable = first_variable
        self.second_variable = second_variable

    def less(self) -> bool:
        return self.first_variable < self.second_variable

    def equal(self) -> bool:
        return self.first_variable == self.second_variable

    def greater(self) -> bool:
        return self.first_variable > self.second_variable

    def notequal(self) -> bool:
        return self.first_variable != self.second_variable
    
    def lessorequal(self) -> bool:
        return self.first_variable <= self.second_variable

    def greaterorequal(self) -> bool:
        return self.first_variable >= self.second_variable

    
# def calculate_strategy(target_product):
#     from strategy.models import StrategyOperation
#     strategy = target_product.strategy
#     data_strategy = {
#         "strategy": strategy.title + str(strategy.id),
#         "strategy_operation": {
#             "operations": StrategyOperation.objects.filter(strategy=strategy).values_list('id')
#         },
#         "strategy_logic_operations"
#     }

# если я создаю первую операцию она не будет привязана к стратегии
# если я создаю первую логическую операцию,
# то вторую я создаю модульку результата, и только после этого я создаю операцию

# рекурсивный парсинг json стратегии, шаг рекурсии 
# если в result находится if 
# по ходу парсинга нужно сразу выявлять нужный result 
# функция должна возвращать нужный result из if или else

# как варинт для монго подключить вторую бд 
# написать модельки используя djongo



def competitors_product_query(self):
        from product.models import CompetitorProduct
        queryset = CompetitorProduct.objects.exclude(competitor=self.strategy.product_strategy.creator)
        return queryset


def median_prices_competitors(self): 
        queryset = self.competitors_product_query
        count_competitors_product = queryset.count()
        values = queryset.product.values_list('current_price_before_discount', flat=True).order_by('current_price_before_discount')
        if count_competitors_product % 2 == 1:
            return values[int(round(count_competitors_product/2))]
        else:
            return sum(values[count_competitors_product/2-1:count_competitors_product/2+1])/Decimal(2.0)


def min_price_competitors(self):
        queryset = self.competitors_product_query
        return queryset.product.aggregate(Min('current_price_before_discount'))


def average_price_competitors(self):
        queryset = self.competitors_product_query
        return queryset.product.aggregate(Avg('current_price_before_discount'))


def max_price_competitors(self):
        queryset = self.competitors_product_query
        return queryset.product.aggregate(Max('current_price_before_discount'))


def price_after_all_discounts(self):
        return self.strategy.product_strategy
