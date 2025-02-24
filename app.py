from flask import Flask, request
import sqlite3
import bcrypt  # Importa la libreria bcrypt per l'hashing delle password

app = Flask(__name__)

@app.route('/utente')
def get_utente():
    utente_id = request.args.get('id')
    db_connection = sqlite3.connect('database.db')
    cursor = db_connection.cursor()

    # Utilizzo di query parametrizzata per prevenire SQL Injection
    query = "SELECT nome, email FROM utenti WHERE id = ?"
    cursor.execute(query, (utente_id,))
    utente = cursor.fetchone()

    db_connection.close()

    if utente:
        return f"Nome: {utente[0]}, Email: {utente[1]}"
    else:
        return "Utente non trovato", 404

if __name__ == '__main__':
    # Inizializzazione database con utenti e amministratori
    conn = sqlite3.connect('database.db')
    cursor = conn.cursor()

    # Creazione tabella utenti con password (in chiaro e hash)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS utenti (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT,
            password_chiaro TEXT,  -- Password memorizzata in chiaro (INSICURO! Solo per demo)
            password_hash TEXT      -- Password memorizzata in hash (SICURO)
        )
    ''')

    # Creazione tabella amministratori con password hash
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS amministratori (
            id INTEGER PRIMARY KEY,
            nome TEXT,
            email TEXT,
            password_hash TEXT      -- Password memorizzata in hash (SICURO)
        )
    ''')

    # Lista di utenti da inserire (con password in chiaro)
    utenti_esempio = [
        ('Mario Rossi', 'mario.rossi@example.com', 'passwordMario'),
        ('Laura Bianchi', 'laura.bianchi@example.com', 'passwordLaura'),
        ('Giovanni Verdi', 'giovanni.verdi@example.com', 'passwordGiovanni'),
        ('Anna Neri', 'anna.neri@example.com', 'passwordAnna'),
        ('Roberto Gialli', 'roberto.gialli@example.com', 'passwordRoberto'),
        ('Francesca Blu', 'francesca.blu@example.com', 'passwordFrancesca'),
        ('Paolo Viola', 'paolo.viola@example.com', 'passwordPaolo'),
        ('Elena Arancio', 'elena.arancio@example.com', 'passwordElena'),
        ('Marco Grigio', 'marco.grigio@example.com', 'passwordMarco'),
        ('Silvia Marroni', 'silvia.marroni@example.com', 'passwordSilvia'),
    ]

    # Inserisci utenti nella tabella, hashando le password con bcrypt
    for nome, email, password_chiaro in utenti_esempio:
        # Hash della password con bcrypt
        password_hash_bytes = bcrypt.hashpw(password_chiaro.encode('utf-8'), bcrypt.gensalt())
        password_hash = password_hash_bytes.decode('utf-8') # Converti bytes in stringa

        cursor.execute("INSERT INTO utenti (nome, email, password_chiaro, password_hash) VALUES (?, ?, ?, ?)",
                       (nome, email, password_chiaro, password_hash)) # Memorizza sia chiaro che hash

    # Lista di amministratori da inserire (con password in chiaro)
    amministratori_esempio = [
        ('Admin Uno', 'admin1@example.com', 'admin1Password'),
        ('Admin Due', 'admin2@example.com', 'admin2Password'),
        ('Admin Tre', 'admin3@example.com', 'admin3Password'),
    ]

    # Inserisci amministratori nella tabella, hashando le password con bcrypt
    for nome, email, password_chiaro in amministratori_esempio:
        # Hash della password con bcrypt
        password_hash_bytes = bcrypt.hashpw(password_chiaro.encode('utf-8'), bcrypt.gensalt())
        password_hash = password_hash_bytes.decode('utf-8') # Converti bytes in stringa

        cursor.execute("INSERT INTO amministratori (nome, email, password_hash) VALUES (?, ?, ?)",
                       (nome, email, password_hash)) # Memorizza solo hash

    conn.commit()
    conn.close()

    app.run(host="0.0.0.0", port=5000, debug=True)  # Assicura che Flask ascolti su tutte le interfacce
