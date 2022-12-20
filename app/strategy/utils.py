from .services import StrategyLogicOperator, StrategyVariable
from datetime import datetime


def strategy_variables(strategy_id):
    return StrategyVariable(strategy_id)


def parse_condition(condidtion: dict, strategy_id: int):
    if_result = StrategyLogicOperator(
                logicals=condidtion["if"]["logicals"],
                variable_object=strategy_variables(strategy_id=strategy_id),
                operand=condidtion['if']['operand'])
    bool_if_result = if_result.calculate()
    print(bool_if_result)
    print(condidtion)
    if bool_if_result:
        if list(condidtion['if']['result'].keys())[0] == "condition":
            parse_condition(condidtion=condidtion['if']['result'], strategy_id=strategy_id)
        return condidtion['if']['result']
    else:
        try:
            if list(condidtion['else']['result'].keys())[0] == "conditional":
                parse_condition(condidtion=condidtion['else']['result'], strategy_id=strategy_id)
            return condidtion['else']['result']
        except KeyError:
            return "Стратегия не имеет else"

def get_needed_strategy_logic(strategy_id: int):
    from strategy.models import Strategy
    from product.models import StrategyProduct
    current_strategy = Strategy.objects.get(id=strategy_id)
    current_strategy_product = StrategyProduct.objects.get(strategy=current_strategy)
    needed_strategy = StrategyProduct.objects.filter(product=current_strategy_product.product).filter(strategy__is_active=True).order_by('strategy__priority').first()
    return needed_strategy.id


def strategy_result(strategy_product_id):
    from product.models import StrategyProduct
    from strategy.models import JournalStrategy
    from strategy.services import StrategyOperator
    from strategy.utils import strategy_variables, parse_condition
    strategy_product = StrategyProduct.objects.get(id=strategy_product_id)
    strategy_result = None
    current_price_before_discount = strategy_product.product.current_price_before_discount

    for i in strategy_product.strategy.logic:
        if list(i.keys()) == ["operations"]:
            strategy_result = i['operations']
        
        if list(i.keys())[0] == "condition":
            ref_dict = i['condition']
            strategy_result = parse_condition(condidtion=ref_dict, strategy_id=strategy_product.strategy.id)

    new_price_by_strategy = StrategyOperator(
        current_price_before_discount=current_price_before_discount,
        variable_object=strategy_variables(strategy_id=strategy_product.strategy.id),
        operations=strategy_result)

    strategy_product.product.new_price_before_discount = new_price_by_strategy.calculate()
    strategy_product.save()
    JournalStrategy.objects.create(
        strategy=strategy_product.strategy,
        journals={
            f"{datetime.now()}": strategy_result
        }
    )