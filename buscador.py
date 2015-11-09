from flask import Flask
from flask import render_template
from flask import request

from buscar import busca
app = Flask(__name__)

@app.route("/")
def buscador():
	searchword = request.args.get('q', '')
	l=busca(searchword)
	return render_template('buscador.html', resultats=l)

if __name__ == "__main__":
    app.run(debug=True)