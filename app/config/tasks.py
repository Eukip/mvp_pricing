from .celery import celery_app
from celery.utils.log import get_task_logger
from datetime import datetime


logger = get_task_logger(__name__)


@celery_app.task
def sample_task():
    logger.info("The sample task just ran.")


@celery_app.task
def strategy_result(strategy_product_id):
    logger.info("The sample task just run.")
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