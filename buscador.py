from flask import Flask
from flask import render_template
from flask import request,jsonify

from buscar import Consultes
from indicadors import Indicadors
app = Flask(__name__)

@app.route("/")
def buscador():
	q = request.args.get('q', '')
	c=Consultes()
	l=c.busca(q)
	return render_template('buscador.html', resultats=l,q=q)

@app.route("/indicadors")
def indicadors():
	return render_template('indicadors.html')	

@app.route("/oberts-mensuals")
def oberts_setmanals():
	c=Consultes()
	return jsonify(c.oberts_mensuals())

@app.route("/oberts-diaris")
def oberts_diaris():
	c=Consultes()
	return jsonify(c.oberts_diaris())	

@app.route("/obrim-setmanals")
def obrim_setmanals():
	c=Consultes()
	return encapsula(c.obrim_setmanals())	

@app.route("/tanquem-setmanals")
def tanquem_setmanals():
	c=Consultes()
	return encapsula(c.tanquem_setmanals())	

@app.route("/tanquem-mensuals")
def tanquem_mensuals():
	c=Consultes()
	return encapsula(c.tanquem_mensuals())		

@app.route("/obrim-mensuals")
def obrim_mensuals():
	c=Consultes()
	return encapsula(c.obrim_mensuals())		

@app.route("/tickets-per-dies-oberts")
def tickets_per_dies_oberts():
	i=Indicadors()
	return encapsula(i.tickets_per_dies_oberts())	

def encapsula(tickets):
	return jsonify({"rows":tickets})


if __name__ == "__main__":
    app.run(debug=True)