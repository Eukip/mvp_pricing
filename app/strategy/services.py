from django.db.models import Max, Min, Avg
from decimal import Decimal
from datetime import datetime


class StrategyVariable(object):

    variables_names = {
        "медианная цена конкурентов": "median_prices_competitors",
        "минимальная цена конкурентов": "min_price_competitors",
        "максимальная цена конкурентов": "max_price_competitors",
        "средняя цена конкурентов": "max_price_competitors",
        "цена после всех скидок": "price_after_all_discounts",
        "today": "today"
    }
    
    def __init__(self, strategy_id) -> None:
        from product.models import CompetitorProduct, Strategy
        self.strategy = Strategy.objects.get(id=strategy_id)
        self.competitor_products = CompetitorProduct.objects.exclude(competitor=self.strategy.product_strategy.creator)
        self.competitor_products_count = self.competitor_products.count()

    @classmethod
    def indirect(self, method_name: str):
        method_name = self.variables_names[method_name]
        method = getattr(self, method_name, lambda : "Такого нету")
        return method()

    def median_prices_competitors(self): 
            values = self.competitor_products.product.values_list('current_price_before_discount', flat=True).order_by('current_price_before_discount')
            if self.competitor_products_count % 2 == 1:
                return values[int(round(self.competitor_products_count/2))]
            else:
                return sum(values[self.competitor_products_count/2-1:self.competitor_products_count/2+1])/Decimal(2.0)

    def min_price_competitors(self):
            queryset = self.competitors_product_query
            return queryset.product.aggregate(Min('current_price_before_discount'))

    def average_price_competitors(self):
            return self.competitor_products.product.aggregate(Avg('current_price_before_discount'))

    def max_price_competitors(self):
            return self.competitor_products.product.aggregate(Max('current_price_before_discount'))

    def price_after_all_discounts(self): # todo доделать цену после всех скидок
            return self.strategy.product_strategy

    def today(self):
        days = {
            "0": "Понедельник",
            "1": "Вторник",
            "2": "Среда",
            "3": "Четверг",
            "4": "Пятница",
            "5": "Суббота",
            "6": "Воскресенье"
        }
        return days[str(datetime.today().weekday())]



class StrategyOperator(object):

    basic_operations = {
        "+": "plus",
        "-": "minus",
        "=": "quation",
        "*": "multiply",
        "/": "divide",
        "+ %": "plus_percent",
        "- %": "minus_percent"
    }

    def __init__(self, current_price_before_discount, variable) -> None:
        self.target_strategy = current_price_before_discount
        self.variable = variable
    
    @classmethod
    def indirect(self, method_name: str):
        method_name = self.basic_operations[method_name]
        method = getattr(self, method_name, lambda : "Такого нету")
        return method()

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
    
    def plus_percent(self) -> int:
        return self.target_strategy - ((self.target_strategy / 100) * self.variable)

    def minus_percent(self) -> int:
        return self.target_strategy + ((self.target_strategy / 100) * self.variable)


class StrategyLogicOperator(object):

    basic_operations = {
        "<": "less",
        "==": "equal",
        ">": "greater",
        "!=": "notequal",
        "<=": "lessorequal",
        ">=": "greaterorequal"
    }

    def __init__(self, first_variable, second_variable) -> None:
        self.first_variable = first_variable
        self.second_variable = second_variable
    
    @classmethod
    def indirect(self, method_name: str):
        method_name = self.basic_operations[method_name]
        method = getattr(self, method_name, lambda : "Такого нету")
        return method()

    def less(self) -> bool:
        return self.first_variable < self.second_variable

    def equal(self) -> bool:
        return self.first_variable == self.second_variable

    def greater(self) -> bool:
        return self.first_variable > self.second_variablestrategy.product_strategy.creator

    def notequal(self) -> bool:
        return self.first_variable != self.second_variable
    
    def lessorequal(self) -> bool:
        return self.first_variable <= self.second_variable

    def greaterorequal(self) -> bool:
        return self.first_variable >= self.second_variable
