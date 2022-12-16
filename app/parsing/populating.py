from app.product.models import Product
from app.parsing.parsing import parse_excel

from itertools import islice


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


def populate_products_excel(article_provider, new_price_before_discount,
                            agreed_discount):
    df = parse_excel()
    row_to_update = df["Артикул поставщика"] == str(article_provider)
    df.loc[row_to_update, "Новая розн. цена (до скидки)"] = new_price_before_discount
    df.loc[row_to_update, "Согласованная скидка, %"] = agreed_discount
    df.to_excel("output.xlsx")
