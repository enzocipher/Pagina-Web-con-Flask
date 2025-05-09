from flask import Flask, render_template, request, session, send_file
import functions as f
import numpy as np
import json
import os

app = Flask(__name__)
app.secret_key = 'MEGATIBURONSIN3950SECRETKEY>ZZZZZZNOROBAR'

#ruta para la carpeta de descargas ahhh
DOWNLOAD_FOLDER = os.path.join(os.getcwd(), 'downloads')
if not os.path.exists(DOWNLOAD_FOLDER):
    os.makedirs(DOWNLOAD_FOLDER)

@app.route('/', methods=['GET', 'POST'])
def index():
    texto = None
    matriz = None
    comparacion = None
    dias = None
    porcentaje = None

    if 'matriz' in session:
        matriz = np.array(json.loads(session['matriz']))

    if request.method == 'POST':
        if 'input_text' in request.form:
            texto = request.form.get('input_text')
            texto = f.validar_numero(texto)
            if type(texto) == int:
                matriz = f.generarconocidos(texto)
                session['matriz'] = json.dumps(matriz.tolist())
                comparacion = f.matrizasivef(matriz)
                dias = None
        elif 'input_porcentaje' in request.form:
            porcentaje = request.form.get('input_porcentaje')
            porcentaje = f.validar_porcentaje(porcentaje)
            if type(porcentaje) == int and matriz is not None:
                dias = f.calcular_dias_contagio(matriz, porcentaje)

    return render_template('index.html', texto=texto, matriz=matriz, comparacion=comparacion, dias=dias, porcentaje=porcentaje)

@app.route('/download', methods=['GET'])
def download():
    if 'matriz' in session:
        matriz = np.array(json.loads(session['matriz']))
        file_path = os.path.join(DOWNLOAD_FOLDER, 'matriz.txt')
        np.savetxt(file_path, matriz, fmt='%d')  # Guardar la matriz en un archivo de texto
        return send_file(file_path, as_attachment=True)
    return "No hay matriz generada para descargar.", 400

if __name__ == '__main__':
    app.run(debug=True, port=8000)