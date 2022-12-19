import requests

def get_wb_catalog_filter_by_query(query):
    catalog_by_query = requests.get(
        url=f'https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&lang=ru&locale=ru&page=1&pricemarginCoeff=1.0&query={query}&reg=0&regions=80,64,83,4,38,33,70,69,86,75,30,40,48,1,22,66,31,68,71&resultset=catalog&sort=priceup&spp=0&suppressSpellcheck=false&xsubject=2223',
    )
    filters_by_query = requests.get(
        url = f"https://search.wb.ru/exactmatch/ru/common/v4/search?appType=1&couponsGeo=12,3,18,15,21&curr=rub&dest=-1029256,-102269,-2162196,-1257786&emp=0&lang=ru&locale=ru&pricemarginCoeff=1.0&query={query}&reg=0&regions=80,64,83,4,38,33,70,69,86,75,30,40,48,1,22,66,31,68,71&resultset=filters&spp=0&suppressSpellcheck=false&xsubject=2223"
    )
    print('Продавцы')
    for j in filters_by_query.json()['data']['filters'][2]['items']:
        print(j)

    print('Цены')
    print(filters_by_query.json()['data']['filters'][3])

    print('Товары')
    for i in catalog_by_query.json()['data']['products']:
        print(i['averagePrice'])
        print(i['brand'])
        print(i['id'])
        print(i['name'])
        print(i['priceU'])
        print(i['salePriceU'])
        print()



def get_seller_by_product_article(article):
    result = []
    while article > 0:
        result.append(article % 10)
        article //= 10

    result.reverse()