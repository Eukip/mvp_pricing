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


    