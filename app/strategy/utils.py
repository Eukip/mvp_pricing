import requests
from product.models import Product, StrategyProduct
from .services import StrategyLogicOperator, StrategyOperator, StrategyVariable
from datetime import datetime


def seacrh_product_by_article(article):
    product_response = requests.get(
        url=f"http://95.217.21.252:8001/products/{article}/"
    )
    if product_response.status_code != 200:
        return "Продукт не найден"
    
    product = Product.objects.create(
        thing=product_response.json()['article']['article']['card']['imt_name'],

    )

    return True

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


def strategy_result(json_field: list[dict], strategy_product):
    from strategy.models import JournalStrategy
    strategy_result = None
    current_price_before_discount = strategy_product.product.current_price_before_discount

    for i in json_field:
        if list(i.keys()) == ["operations"]:
            strategy_result = i['operations']
        
        if list(i.keys())[0] == "condition":
            ref_dict = i['condition']
            strategy_result = parse_condition(condidtion=ref_dict, strategy_id=strategy_product.strategy.id)

    new_price_by_strategy = StrategyOperator(
        current_price_before_discount=current_price_before_discount,
        variable_object=strategy_variables(strategy_id=strategy_product.strategy.id),
        operations=strategy_result).calculate()

    strategy_product.product.new_price_before_discount = new_price_by_strategy
    JournalStrategy.objects.create(
        strategy=strategy_product.strategy,
        journals={
            f"{datetime.now()}": strategy_result
        }
    )

def get_needed_strategy_logic(strategy_id: int):
    from strategy.models import Strategy
    current_strategy = Strategy.objects.get(id=strategy_id)
    current_strategy_product = StrategyProduct.objects.get(strategy=current_strategy)
    needed_strategy = StrategyProduct.objects.filter(product=current_strategy_product.product).fitler(strategy__is_active=True).order_by('strategy__priority').first()
    return needed_strategy
