# place for recursion func
# рекурсивный парсинг json стратегии, шаг рекурсии 
# если в result находится if 
# по ходу парсинга нужно сразу выявлять нужный result 
# функция должна возвращать нужный result из if или else

# как варинт для монго подключить вторую бд 
# написать модельки используя djongo
import requests
from product.models import Product

def seacrh_product_by_article(article):
    product_response = requests.get(
        url=f"http://95.217.21.252:8001/products/{article}/"
    )
    if product_response.status_code != 200:
        return "Продукт не найден"
    
    product = Product.objects.create(
        thing=product_response.json()['article']['article']['card']['imt_name'],

    )
