from flask import Flask, request
import os 


app = Flask(__name__)

@app.route('/receive_file', methods=['POST'])
def ricevi_file():
    try:
        file = request.files['file']

        # Specifica il percorso in cui salvare il file ricevuto
        nome_file_ricevuto = file.filename
        percorso_completo = os.path.join(os.path.join(os.path.expanduser('~'), 'Desktop/ricevuti'), nome_file_ricevuto)

        # Salva il file ricevuto
        file.save(percorso_completo)

        print(f'File ricevuto con successo: {percorso_completo}')

        return 'File ricevuto con successo.'

    except Exception as e:
        print(f'Errore durante il ricevimento del file: {e}')
        return 'Errore durante il ricevimento del file.'

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=4444)
