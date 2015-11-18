from flask import Flask
from flask import render_template
from flask import request,jsonify

from buscar import Consultes
app = Flask(__name__)

@app.route("/")
def buscador():
	q = request.args.get('q', '')
	c=Consultes()
	l=c.busca(q)
	return render_template('buscador.html', resultats=l,q=q)

@app.route("/oberts-setmanals")
def oberts_setmanals():
	c=Consultes()
	return jsonify(c.oberts_setmanals())


if __name__ == "__main__":
    app.run(debug=True)