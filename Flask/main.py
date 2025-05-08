# app.py
from flask import Flask, render_template, request
import functions as f 

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        texto = None
        matriz=None
        comparacion=None
    if request.method == 'POST':
        texto = request.form.get('input_text')
        texto = f.validar_numero(texto)
        if type(texto) == int:
            matriz = f.generarconocidos(texto)
            matriz2 = matriz
            matriz = matriz.tolist()
            comparacion = f.matrizasivef(matriz2)
        else:
            matriz = None
            comparacion = None
    return render_template('index.html', texto=texto, matriz=matriz, comparacion=comparacion)

if __name__ == '__main__':
    app.run(debug=True, port = 8000)