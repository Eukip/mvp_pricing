from .services import StrategyLogicOperator, StrategyOperator, StrategyVariable

from datetime import datetime

def logical_operators(operation, *args):
    if operation == "or":
        for item in args:
            if item:
                return True
    if operation == "and":
        for item in args:
            if not item:
                return False
    return True


def strategy_calculation(json_field, strategy_id):

    if list(json_field[0].keys())[0] == "operations":
        return {"result": json_field[0]}

    strategy = StrategyVariable(strategy_id)

    ref_dict = json_field[0]["condition"]
    operand = ref_dict["if"]["operand"]
    logicals = ref_dict["if"]["logicals"]
    conditions = tuple()
    for logic in range(len(logicals)):
        method_name = logicals[logic]["variables"][0]
        method = strategy.indirect(method_name)
        operation = logicals[logic]["operation"]
        comparison = StrategyLogicOperator(method, logicals[logic]["variables"][1])
        conditions = conditions + (comparison.indirect(operation), )

    if logical_operators(operand, conditions):
        return ref_dict["if"]["result"]

    return ref_dict["else"]


def result_calculation(result_json, strategy_id, current_price_before):
    strategy = StrategyVariable(strategy_id)
    operations = result_json["operations"]
    current_price_after = current_price_before
    for step in range(len(operations)):
        variable = strategy.indirect(operations[step]["variable"])
        operation = strategy_operation.indirect(operations[step]["do"])
        strategy_operation = StrategyOperator(current_price_after, variable)
        current_price_after = strategy_operation.indirect(operation)
        strategy.strategy.journals[datetime.now()] = [{f"operation_{datetime.now()}": {current_price_before}}]
        strategy.strategy.save()
    return current_price_after


def df():
    var = [{"condition": {
                "if": {
                    "logicals": [{
                        "variables": ["today", "Суббота"],
                        "operation": "=="
                    },
                    {
                        "variables": ["today", "Воскресенье"],
                        "operation": "=="
                    }],
                    "operand": "or",
                    "result": {
                        "operations": [{
                            "variable": "MIN_PRICE_C",
                            "do": "="
                        },
                        {
                            "variable": 3,
                            "do": "- %"
                        }]
                    }
                },
                "else": {
                    "result": {
                        "operations": [{
                            "variable": "MOST_POPULAR_PRICE_C",
                            "do": "EQUAL"
                        }]
                    }
                }
            }
        }]
    return var

def df1():
    return [{"operations": [{
                            "variable": "MIN_PRICE_C",
                            "do": "="
                        },
                        {
                            "variable": 3,
                            "do": "- %"
                        }]}]

def df2():
    var = [{"operations": [{
                "variable": "медианная цена конкурентов",
                "do": "="
            }]}]
    return var

def df3():
    var = [{
            "operations": [
                    {
                        "variable":"минимальная цена конкурентов",
                        "do": "="
                    },
                    {
                        "variable": 10,
                        "do": "-"
                    }
            ]
        }]
    return var

def df4():
    var = [
            {
                "operations": [
                    {
                        "variable": "минимальная цена конкурентов",
                        "do": "="
                    },
                    {
                        "variable": 5,
                        "do": "- %"
                    }
                ]
            }
        ]
    return var

def df5():

    var = [
            {
                "condition": {
                    "if": {
                        "logicals": [
                            {
                                "variable": ["цена после всех скидок", "РРЦ"],
                                "operation": ">="
                            }
                        ],
                        "operand": "null",
                        "result": {
                            "operations": [
                                {
                                    "variable": "минимальная цена конкурентов",
                                    "do": "="
                                },
                                {
                                    "variable": 20,
                                    "do": "-"
                                }
                            ]
                        }
                    }
                }
            }
        ]
    return var