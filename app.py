from flask import render_template, Flask, request

import dao
app = Flask(__name__)


@app.route('/')
def index():
    cate_id = request.args.get('category_id')
    product_name = request.args.get('name')
    prods = dao.load_products(cate_id=cate_id, name=product_name)
    return render_template('index.html', products=prods)


@app.route('/products/<int:id>')
def details(id):
    product = dao.get_product_by_id(product_id=id)
    return render_template('product-details.html', product=product)


# @app.route('/login')
# def login_my_user():


@app.context_processor
def common_attrib():
    return {"categories" : dao.load_categories()}


if __name__ == '__main__':
    app.run(debug=True)

