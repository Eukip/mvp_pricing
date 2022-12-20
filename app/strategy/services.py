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
        "today": "today",
        "РРЦ": "rrc"
    }

    strategy = None
    competitor_products = None
    competitor_products_count = None

    @classmethod
    def __init__(self, strategy_id) -> None:
        from product.models import CompetitorProduct, Strategy
        self.strategy = Strategy.objects.get(id=strategy_id)
        print(self.strategy.sp_strategy.get().product)
        self.competitor_products = CompetitorProduct.objects.exclude(product=self.strategy.sp_strategy.get().product)
        self.competitor_products_count = self.competitor_products.count()


    @classmethod
    def indirect(self, method_name):
        if type(method_name) == int:
            return method_name
        method_name = self.variables_names[method_name]
        method = getattr(self, method_name, lambda : "Такого нету")
        return method()

    @classmethod
    def median_prices_competitors(self): 
            values = self.competitor_products.values_list('product__current_price_before_discount', flat=True).order_by('product__current_price_before_discount')
            print(values)
            if self.competitor_products_count % 2 == 1:
                return values[int(round(self.competitor_products_count/2))]
            else:
                return sum(values[self.competitor_products_count/2-1:self.competitor_products_count/2+1])/Decimal(2.0)

    @classmethod
    def min_price_competitors(self):
        queryset = self.competitor_products
        print(self.competitor_products)
        return queryset.aggregate(Min('product__current_price_before_discount'))
    
    @classmethod
    def average_price_competitors(self):
        return self.competitor_products.product.aggregate(Avg('current_price_before_discount'))

    @classmethod
    def max_price_competitors(self):
        return self.competitor_products.product.aggregate(Max('current_price_before_discount'))

    @classmethod
    def price_after_all_discounts(self):
        return self.strategy.sp_strategy.get().product.price_after_dicount

    @classmethod
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
    
    @classmethod
    def rrc(self):
        return self.strategy.sp_strategy.get().product.price_after_dicount



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

    result = None
    bar = None
    foo = None

    operations = None
    variable_object = None
    target_strategy = None
    
    
    @classmethod
    def __init__(self, current_price_before_discount: int, variable_object: object, operations: list[dict]) -> None:
        self.target_strategy = current_price_before_discount
        self.variable_object = variable_object
        self.operations = operations
    
    @classmethod
    def calculate(self):
        print(self.operations)
        for i in self.operations['operations']:
            print(i)
            self.foo = self.variable_object.indirect(i['variable'])
            self.bar = self.target_strategy
            method_name = self.basic_operations[i['do']]
            getattr(self, method_name, lambda : "Такого нету")
        return self.result

    @classmethod
    def plus(self) -> int:
        self.result = self.bar + self.foo
        return self.result
    
    @classmethod
    def minus(self) -> int:
        self.result = self.bar - self.foo
        return self.result

    @classmethod
    def multiply(self) -> int:
        self.result = self.bar * self.foo
        return self.result
    
    @classmethod
    def divide(self) -> int:
        self.result = self.bar / self.foo
        return self.result
    
    @classmethod
    def plus_percent(self) -> int:
        self.result = self.bar - ((self.bar / 100) * self.foo)
        return self.result

    @classmethod
    def minus_percent(self) -> int:
        self.result = self.bar + ((self.bar / 100) * self.foo)
        return self.result


class StrategyLogicOperator(object):

    basic_operations = {
        "<": "less",
        "==": "equal",
        ">": "greater",
        "!=": "notequal",
        "<=": "lessorequal",
        ">=": "greaterorequal"
    }

    basic_operands = {
        "or": "method_or",
        "and": "method_and"
    }

    foo = None
    bar = None

    operand_variables = []

    result = False

    first_variable = None
    second_variable = None

    logicals = None

    @classmethod
    def __init__(self, logicals:list[dict], variable_object: object, operand:str) -> None:
        self.logicals = logicals
        self.variable_object = variable_object
        self.operand = operand
        
    @classmethod
    def calculate(self):
        for i in self.logicals:
            print(i)
            self.first_variable = self.variable_object.indirect(i['variable'][0])
            self.second_variable = self.variable_object.indirect(i['variable'][1])
            calculate_method_name = self.basic_operations[i['operation']]
            getattr(self, calculate_method_name, lambda: Exception)
        for j in range(len(self.operand_variables) - 1):
            self.foo = self.operand_variables[j] 
            self.bar = self.operand_variables[j + 1]
            self.result = getattr(self, self.basic_operands[self.operand], lambda: Exception)
        return self.result

    @classmethod
    def less(self) -> bool:
        result = self.first_variable < self.second_variable
        return self.operand_variables.append(result)

    @classmethod
    def equal(self) -> bool:
        result = self.first_variable == self.second_variable
        return self.operand_variables.append(result)

    @classmethod
    def greater(self) -> bool:
        result = self.first_variable > self.second_variable
        return self.operand_variables.append(result)

    @classmethod
    def notequal(self) -> bool:
        result = self.first_variable != self.second_variable
        return self.operand_variables.append(result)
    
    @classmethod
    def lessorequal(self) -> bool:
        result = self.first_variable <= self.second_variable
        return self.operand_variables.append(result)

    @classmethod
    def greaterorequal(self) -> bool:
        result = self.first_variable >= self.second_variable
        return self.operand_variables.append(result)

    @classmethod
    def method_or(self) -> bool:
        self.result = self.foo or self.bar
        return self.result 
    @classmethod
    def method_and(self) -> bool:
        self.result = self.foo and self.bar
        return self.result
