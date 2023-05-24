from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

	data = {
	'titulo': 'DELIVERY PREDICTOR',
	'area': 'Metrología'
	}

	return render_template('index.html', data=data)

@app.route('/como_funciona')
def como_funciona():

	data = {
	'titulo': '¿CÓMO FUNCIONA?',
	'area': 'Metrología'
	}

	return render_template('como_funciona.html', data=data)

def pagina_no_encontrada(error):

	data = {
	'titulo': 'Uuuupss... Creo que te equivocaste :-(',
	'area': 'Metrología'
	}

	return render_template('pagina_no_encontrada.html', data=data), 404

if  __name__ == '__main__':
	app.register_error_handler(404, pagina_no_encontrada)
	app.run(debug=True, port=5000)