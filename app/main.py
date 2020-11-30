from catalog import get_products, create_product
from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/product', methods=['GET', 'POST'])
def list_all_products():
	'''This view manages the CRUD of products'''
	if request.method == 'GET':
		response = get_products()
		return jsonify(response)

	if request.method == 'POST':
		data = request.get_json()
		create_product(
			data['sku'],
			data['title'],
			data['long_description'],
			data['price_euro'])
		return jsonify({"status": "ok"})

@app.route('/hello')

def hello_world():
	message = "Hola mundo, soy Python! Ahora con CloudBuild"
	response = {
		"message": message,
		"length": len(message)
	}
	return jsonify(response)

@app.route('/bye')

def bye_world():
    return 'Bye, World!'

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')
