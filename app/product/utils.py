import os
import pandas as pd
from itertools import islice
from product.models import Product


def parse_excel():
    # todo create func paramter for file
    df = pd.read_excel(os.getcwd() + "/app/product/7eb50656ea82adcb.xlsx")
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


def populate_excel(data):
    df = pd.read_excel(os.getcwd() + "/app/product/7eb50656ea82adcb.xlsx")
    for item in data:
        print(item.keys())
        item_key = list(item.keys())[0]
        row_to_update = df["Артикул поставщика"] == str(item_key)
        df.loc[row_to_update, "Новая розн. цена (до скидки)"] = item[item_key]["new_price"]
        df.loc[row_to_update, "Согласованная скидка, %"] = item[item_key]["agreed_discount"]
    df.to_excel("output.xlsx")


def populate_products_db():
    data = parse_excel()
    data_keys = data.keys()
    batch_size = len(data_keys)
    objs = (Product(thing=data[key]["Бренд"],
                    vendor_code=data[key]["Предмет"],
                    article_provide=data[key]["Артикул поставщика"],
                    nomenclature_lc_code=data[key]["Номенклатура (код 1С)"],
                    last_barcode=data[key]["Последний баркод"],
                    remainder=data[key]["Остаток товара (шт.)"],
                    current_price_before_discount=data[key]["Текущая розн. цена (до скидки)"],
                    new_price_before_discount=data[key]["Новая розн. цена (до скидки)"],
                    current_discount=data[key]["Текущая скидка на сайте, %"],
                    recommended_discount=data[key]["Рекомендованная скидка, %"],
                    agreed_discount=data[key]["Согласованная скидка, %"],
                    cuurent_discount_promo=data[key]["Текущая скидка по промокоду, %"],
                    new_discount_promo=data[key]["Новая скидка по промокоду, %"])
            for key in data_keys)
    batch = list(islice(objs, batch_size))
    if not batch:
        print("No batch created")
    Product.objects.bulk_create(batch, batch_size)