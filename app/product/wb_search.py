import requests

def get_wb_catalog_filter_by_query(query: str):
    query = query.replace(' ', '%').upper()
    catalog_by_query = requests.get(
        url=f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&lang=ru&locale=ru&page=1&pricemarginCoeff=1.0&query={query}&reg=0&regions=80,64,83,4,38,33,70,69,86,75,30,40,48,1,22,66,31,68,71&resultset=catalog&sort=priceup&spp=0&suppressSpellcheck=false&xsubject=2223',
    )
    filters_by_query = requests.get(
        url = f"https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&lang=ru&locale=ru&pricemarginCoeff=1.0&query={query}&reg=0&regions=80,64,83,4,38,33,70,69,86,75,30,40,48,1,22,66,31,68,71&resultset=filters&spp=0&suppressSpellcheck=false&xsubject=2223"
    )
    print(filters_by_query)
    print(catalog_by_query)
    result = {
        "maxPriceU": filters_by_query.json()['data']['filters'][3]['maxPriceU'],
        "minPriceU": filters_by_query.json()['data']['filters'][3]['minPriceU'],
        "items": []
    }

    for i in catalog_by_query.json()['data']['products']:
        product = {
            # "averagePrice": i['averagePrice'],
            "brand": i['brand'],
            "article": i['id'],
            "name": i['name'],
            "priceU": i['priceU'],
            "salePriceU": i['salePriceU']
        }
        result['items'].append(product)

    return result


def get_seller_by_product_article(article: int):
    result = []
    while article > 0:
        result.append(article % 10)
        article //= 10

    result.reverse()
    vol = 0
    part = 0
    article = 0
    if len(result) == 8:

        for i, v in enumerate(reversed(result[slice(3)])):
            vol += v * 10 ** i
        
        for i, v in enumerate(reversed(result[slice(5)])):
            part += v * 10 ** i

        for i, v in enumerate(reversed(result)):
            article += v * 10 ** i
    
    if len(result) == 9:

        for i, v in enumerate(reversed(result[slice(4)])):
            vol += v * 10 ** i
        
        for i, v in enumerate(reversed(result[slice(6)])):
            part += v * 10 ** i

        for i, v in enumerate(reversed(result)):
            article += v * 10 ** i
    
    services_numbers = "01", "02", "03", "04", "05", "06", "07", "08", "09", "10"
    
    for i in services_numbers:
        seller = requests.get(
            url=f"https://basket-{i}.wb.ru/vol{vol}/part{part}/{article}/info/sellers.json"
        )
        if seller.status_code == 200:
            return seller.json()
    return "Not found"


def get_product_by_article(article: int):
    product = requests.get(
        url = f"https://card.wb.ru/cards/detail?spp=0&regions=80,64,83,4,38,33,70,69,86,75,30,40,48,1,22,66,31,68,71&pricemarginCoeff=1.0&reg=0&appType=1&emp=0&locale=ru&lang=ru&curr=rub&couponsGeo=12,3,18,15,21&dest=-1029256,-102269,-2162196,-1257786&nm={article}"
    )
    if product.status_code != 200:
        return "Not found"
    return product.json()['data']['products'][0]
