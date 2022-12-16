# from app.config.settings import BASE_DIR

import pandas as pd

import os


def parse_excel():
    df = pd.read_excel(os.getcwd() + "/app/parsing/7eb50656ea82adcb.xlsx")
    result = {}
    for item in range(1, len(df)):
        temp_dict = {"Бренд": df["Бренд"][item - 1],
                     "Артикул поставщика": df["Артикул поставщика"][item - 1],
                     "Предмет": df["Предмет"][item - 1],
                     "Коллекция": df["Коллекция"][item - 1],
                     "Номенклатура (код 1С)": df["Номенклатура (код 1С)"][item - 1],
                     "Последний баркод": df["Последний баркод"][item - 1],
                     "Количество дней на сайте": df["Количество дней на сайте"][item - 1],
                     "Неликвид": df["Неликвид"][item - 1],
                     "Дата появления неликвида": df["Дата появления неликвида"][item - 1],
                     "Оборачиваемость": df["Оборачиваемость"][item - 1],
                     "Остаток товара (шт.)": df["Остаток товара (шт.)"][item - 1],
                     "Текущая розн. цена (до скидки)": df["Текущая розн. цена (до скидки)"][item - 1],
                     "Новая розн. цена (до скидки)": df["Новая розн. цена (до скидки)"][item - 1],
                     "Текущая скидка на сайте, %": df["Текущая скидка на сайте, %"][item - 1],
                     "Рекомендованная скидка, %": df["Рекомендованная скидка, %"][item - 1],
                     "Согласованная скидка, %": df["Согласованная скидка, %"][item - 1],
                     "Текущая скидка по промокоду, %": df["Текущая скидка по промокоду, %"][item - 1],
                     "Новая скидка по промокоду, %": df["Новая скидка по промокоду, %"][item - 1],
                     }
        result["item_" + str(item)] = temp_dict
    return result


def populate_products_excel(article_provider, new_price_before_discount,
                            agreed_discount):
    df = pd.read_excel(os.getcwd() + "/app/parsing/7eb50656ea82adcb.xlsx")
    row_to_update = df["Артикул поставщика"] == str(article_provider)
    df.loc[row_to_update, "Новая розн. цена (до скидки)"] = new_price_before_discount
    df.loc[row_to_update, "Согласованная скидка, %"] = agreed_discount
    df.to_excel("output.xlsx")


def populate_excel(data):
    df = pd.read_excel(os.getcwd() + "/app/parsing/7eb50656ea82adcb.xlsx")
    for item in data:
        print(item.keys())
        item_key = list(item.keys())[0]
        row_to_update = df["Артикул поставщика"] == str(item_key)
        df.loc[row_to_update, "Новая розн. цена (до скидки)"] = item[item_key]["new_price"]
        df.loc[row_to_update, "Согласованная скидка, %"] = item[item_key]["agreed_discount"]
    df.to_excel("output.xlsx")


var = [{
    '7st_351144_030864-WN79/1': {
        'new_price': 100,
        'agreed_discount': 10
    }
},
    {
        'buy2_N1ME0144/1': {
            'new_price': 100,
            'agreed_discount': 10
        }
    }
]
