from flask import Flask
from flask import render_template
from flask import request

from buscar import busca
app = Flask(__name__)

@app.route("/")
def buscador():
	q = request.args.get('q', '')
	l=busca(q)
	return render_template('buscador.html', resultats=l,q=q)

if __name__ == "__main__":
    app.run(debug=True)