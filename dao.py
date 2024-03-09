import json


def load_categories():
    with open('data/categories.json', encoding='utf-8') as f:
        return json.load(f)


def load_products(cate_id=None, name=None):
    with open('data/products.json', encoding='utf-8') as f:
        products = json.load(f)
        if cate_id:
            products = [p for p in products if p['category_id'].__eq__(int(cate_id))]

        if name:
            products = [p for p in products if p['name'].find(name) >= 0]

    return products


def get_product_by_id(product_id=None):
    with open('data/products.json', encoding='utf-8') as f:
        products = json.load(f)
        for p in products:
            if p['id'] == product_id:
                return p


if __name__ == '__main__':
    load_categories()

