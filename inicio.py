from flask import Flask, render_template, url_for, request

app = Flask(__name__)

@app.route('/inicio')
def index():
    return render_template('index.html', titulo='Bem Vindo')

@app.route('/converter', methods=['POST',])
def converter():
    texto_um = request.form['texto_um']
    return render_template('index.html', titulo='Pronto', texto=texto_um)

app.run(debug=True)