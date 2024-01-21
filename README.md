# KeyRoll - Python Keylogger for Red Teaming

![Keyroll-removebg-preview](https://github.com/HydraHackerSec/KeyRoll/assets/157287105/888b195e-0958-47ad-ae12-9a519b2bc40f)


**Disclaimer: L'uso di KeyRoll è consentito esclusivamente a fini educativi e nel rispetto delle leggi vigenti. Gli sviluppatori di KeyRoll declinano ogni responsabilità per utilizzi impropri o illegali del software.**

## Descrizione

KeyRoll è un keylogger sviluppato in Python come parte di un progetto scolastico per il corso di Red Teaming presso la nostra scuola di Cyber Security. Il software è stato creato da due studenti, [Carioni Federico](https://github.com/troclea) e [Torchia Vincenzo](https://github.com/BinxSake), con la collaborazione di [Benedetti Denis](https://github.com/DB02Archery) e Mazzola Giorgio

## Funzionalità Principali

- **Registrazione Tasti**: KeyRoll è in grado di registrare la tastiera dell'utente e salvare i dati in un file di log.
- **Modalità Silenziosa**: Il keylogger opera in background senza mostrare segni evidenti di attività.
- **Easter Egg**: KeyRoll contiene un easter egg nascosto all'interno del codice, che offre un tocco divertente al progetto.

## Requisiti del Sistema

- Python 3.x
- Sistemi Operativi: Windows, Linux

## Istruzioni per l'Utilizzo

1. Assicurarsi di avere Python 3 installato sul sistema.
2. Clonare il repository: `git clone https://github.com/tuonome/KeyRoll.git`
3. Eseguire il programma: `keyroll.py`
4. Il keylogger inizierà a registrare la tastiera e salverà i log in un file e lo invierà a un server in ascolto.

## Contributi e Segnalazione Bug

Siamo aperti a contributi e miglioramenti. Se trovi bug o hai suggerimenti, apri una nuova issue su GitHub.

## Disclaimer

KeyRoll è stato creato a scopo educativo e per consentire agli studenti di comprendere le minacce potenziali relative ai keylogger. Non incoraggiamo né supportiamo l'uso illecito o dannoso di questo software. Gli sviluppatori non si assumono alcuna responsabilità per qualsiasi conseguenza derivante dall'uso improprio di KeyRoll.

**Usa il software in modo responsabile e legale.**

---

*Nota: Il progetto KeyRoll è stato realizzato a fini educativi e non deve essere utilizzato in modo illecito o senza il consenso dell'utente interessato. Il disclaimer è incluso per chiarire che gli sviluppatori non intendono promuovere attività illegali o dannose.*

# Table of contents:

<table>
<thead>
  <tr>
    <th>Classe<br></th>
    <th>Funzione</th>
    <th>Nome</th>
    <th>Scritto<br></th>
    <th>Testato (Windows)</th>
    <th>Implementato</th>
    <th>Note</th>
  </tr>
</thead>
<tbody>
  <tr>
    <td rowspan="2" style="text-orientation: mixed;">CustomDescritionFormatter(argparse.RawDescriptionHelpFormatter)</td>
    <td>Massima lunghezza linea</td>
    <td>_init_</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Argparse nuova linea<br></td>
    <td>_split_lines<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="2" style="text-orientation: mixed;">Keyboard<br></td>
    <td>Quando viene premuto un pulsante</td>
    <td>on_key_press</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Quando viene rilasciato un pulsante</td>
    <td>on_key_release<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="3" style="text-orientation: mixed;">Mouse</td>
    <td>Quando viene premuto un pulsante del mouse</td>
    <td>on_mouse_click<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Quando il mouse effettua uno scroll</td>
    <td>on_mouse_scroll<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Quando il mouse si muove</td>
    <td>on_mouse_move<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="8" style="text-orientation: mixed;">Util</td>
    <td>Controllo ip<br></td>
    <td>is_valid_ip<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Rimozione dell'ultimo log inviato</td>
    <td>log_path_size<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Interrupt di uscita</td>
    <td>controlled_exit<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Gestione interrupt di uscita</td>
    <td>sigint_handler</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Cerca la directory di dove salvare i log</td>
    <td>log_dir_find<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Crea la directory dove salvare i log</td>
    <td>log_dir_create</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Costruzione un nome per file con data e ora UTC<br></td>
    <td>UTC_filename</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Cerca il file di log</td>
    <td>get_log_file<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="6" style="text-orientation: mixed;">Key_special_function</td>
    <td>Mappa tasti non riconosciuti</td>
    <td>keyboard_codes_mapping<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Mappa tasti non riconosciuti che iniziano con \</td>
    <td>windows_keyboard_codes_mapping<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Controlla se il tasto premuto è destro o sinistro</td>
    <td>left_or_right</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Stampa messaggio di taglia<br></td>
    <td>handle_cut</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Stampa messaggio di copia</td>
    <td>handle_copy</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Stampa messaggio di incolla</td>
    <td>handle_paste</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="5" style="text-orientation: mixed;">Trigger</td>
    <td>Chiama una funzione da una stringa</td>
    <td>call_global_function<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Quando viene digitata una parola</td>
    <td>class Special_word</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Quando path supera peso</td>
    <td>class Over_size</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Funzione richiamata ad intervalli (async)<br></td>
    <td>class Recursive_interval</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Prima di spegnimento<br></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Preso in considerazione<br></td>
  </tr>
  <tr>
    <td rowspan="9" style="text-orientation: mixed;">Spy<br></td>
    <td>Fa uno screenshot</td>
    <td>screenshot<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Fa una foto</td>
    <td>photo</td>
    <td>Si<br></td>
    <td>No<br></td>
    <td>No</td>
    <td></td>
  </tr>
  <tr>
    <td>Fa il dump dei processi</td>
    <td>process</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Fa il dump delle NIC</td>
    <td>web</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Ritorna grandezza schermo</td>
    <td>screen_size</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Fa il dump dei dischi<br></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Preso in considerazione<br></td>
  </tr>
  <tr>
    <td>Fa il dump della CPU<br></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Preso in considerazione<br></td>
  </tr>
  <tr>
    <td>Microfono<br></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Preso in considerazione<br></td>
  </tr>
  <tr>
    <td>Dispositivi USB<br></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Preso in considerazione<br></td>
  </tr>
  <tr>
    <td rowspan="6" style="text-orientation: mixed;">Log<br></td>
    <td>Crea il messaggio</td>
    <td>create_message</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Crea il messaggio di errore fatale</td>
    <td>error</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Stampa il messaggio a schermo</td>
    <td>print_message</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Stampa il messaggio su file di log</td>
    <td>print_file</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Crea nuovo file di log</td>
    <td>configure_print_file</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Trova vecchi file di log</td>
    <td>find_old_file</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="6" style="text-orientation: mixed;">Sender<br></td>
    <td>Controlla la connessione</td>
    <td>check_connection<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Invia tramite richiesta post<br></td>
    <td>send_file_via_http<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Invia tramite ftp<br></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Preso in considerazione<br></td>
  </tr>
  <tr>
    <td>Invia tramite mail<br></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Preso in considerazione<br></td>
  </tr>
  <tr>
    <td>Invio in streaming<br></td>
    <td></td>
    <td></td>
    <td></td>
    <td></td>
    <td>Preso in considerazione<br></td>
  </tr>
  <tr>
    <td>Invia il messaggio e rinomia il file di log</td>
    <td>sender</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td rowspan="2" style="text-orientation: mixed;">global space</td>
    <td>-</td>
    <td>main</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td></td>
  </tr>
  <tr>
    <td>Controlla OS se eseguibile imposta autoesecuzione e riavvia</td>
    <td>pre_main</td>
    <td>Si<br></td>
    <td>Si<br></td>
    <td>Si</td>
    <td></td>
  </tr>
</tbody>
</table>

*Nota: KeyRoll è stato testato su Windows e risulta funzionante*



# Come installare i requirements:

Per installare i pacchetti elencati nel file requirements.txt, puoi utilizzare il comando pip. Assicurati di trovarmi nella directory che contiene il tuo file requirements.txt, quindi esegui il seguente comando nel tuo terminale o prompt dei comandi:

```bash
pip install -r requirements.txt
```
Questo comando installerà tutti i pacchetti elencati nel file requirements.txt e le relative dipendenze. Assicurati di avere pip installato e che sia aggiornato alla versione più recente. Se non hai ancora installato pip, puoi farlo seguendo le istruzioni nel sito web di Python: https://pip.pypa.io/en/stable/installation/

Una volta completata l'installazione, il tuo ambiente dovrebbe essere pronto con tutte le dipendenze necessarie.


# Compilare il codice con PyInstaller:

Per installare pyinstaller, puoi utilizzare il comando pip come segue:

```bash
pip install pyinstaller
```

Una volta installato pyinstaller, puoi utilizzare il comando che hai fornito per creare un eseguibile standalone del tuo script Python. Assicurati di essere nella directory del tuo script prima di eseguire questo comando. Se stai utilizzando un terminale Windows, sostituisci py con python nel comando. Ecco il comando aggiornato:

```bash
python -m PyInstaller "path/to/key.py" --onefile --icon "path/to/keyroll.ico" --name "KeyRoll" -w
```

Assicurati di fornire i percorsi corretti ai tuoi file (key.py, l'icona, ecc.) nei comandi sopra.

Inoltre, tieni presente che il flag -w nel comando indica di eseguire l'app in modalità GUI senza aprire una finestra del terminale. Se preferisci visualizzare l'output del tuo script, puoi rimuovere questo flag.

Dopo aver eseguito il comando, troverai il tuo eseguibile nella directory dist all'interno della directory del tuo progetto.


# Compatibilità

- **Windows**: compatibile, stabile e testato
- **Linux, debian based**: compatibile, stabile e testato

