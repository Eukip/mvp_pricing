from .services import StrategyLogicOperator, StrategyVariable


def strategy_variables(strategy_id):
    return StrategyVariable(strategy_id)


def parse_condition(condidtion: dict, strategy_id: int):
    if_result = StrategyLogicOperator(
                logicals=condidtion["if"]["logicals"],
                variable_object=strategy_variables(strategy_id=strategy_id),
                operand=condidtion['if']['operand'])
    if if_result.calculate():
        if list(condidtion['if']['result'].keys())[0] == "condition":
            parse_condition(condidtion=condidtion['if']['result'], strategy_id=strategy_id)
        return condidtion['if']['result']
    else:
        if list(condidtion['else']['result'].keys())[0] == "conditional":
            parse_condition(condidtion=condidtion['else']['result'], strategy_id=strategy_id)
        return condidtion['else']['result']


def get_needed_strategy_logic(strategy_id: int):
    from strategy.models import Strategy
    from product.models import StrategyProduct
    current_strategy = Strategy.objects.get(id=strategy_id)
    current_strategy_product = StrategyProduct.objects.get(strategy=current_strategy)
    needed_strategy = StrategyProduct.objects.filter(product=current_strategy_product.product).fitler(strategy__is_active=True).order_by('strategy__priority').first()
    needed_strategy_product_object = StrategyProduct.objects.filter(strategy=needed_strategy)
    return needed_strategy_product_object
