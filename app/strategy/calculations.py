from .services import StrategyLogicOperator

def strategy_calculation(json_field):

    if list(json_field[0].keys())[0] == "operations":
        return {"result": json_field[0]}

    ref_dict = json_field[0]["condition"]
    return ref_dict





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