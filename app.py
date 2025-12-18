from flask import Flask, render_template, request, redirect, jsonify, url_for
import sqlite3
import string
import random
import qrcode
import io
import base64

app = Flask(__name__)

# --- Database Setup ---
def init_db():
    with sqlite3.connect('database.db') as conn:
        conn.execute('CREATE TABLE IF NOT EXISTS urls (id INTEGER PRIMARY KEY AUTOINCREMENT, original_url TEXT, short_id TEXT UNIQUE)')

def get_db_connection():
    conn = sqlite3.connect('database.db')
    conn.row_factory = sqlite3.Row
    return conn

# --- Helper Functions ---
def generate_short_id(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(length))

# --- Routes ---
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/shorten', methods=['POST'])
def shorten_url():
    data = request.get_json()
    original_url = data.get('url')
    
    if not original_url:
        return jsonify({'error': 'URL is required'}), 400

    conn = get_db_connection()
    
    # Check if already exists to save space (optional)
    existing = conn.execute('SELECT short_id FROM urls WHERE original_url = ?', (original_url,)).fetchone()
    if existing:
        short_id = existing['short_id']
    else:
        short_id = generate_short_id()
        # Ensure uniqueness
        while conn.execute('SELECT id FROM urls WHERE short_id = ?', (short_id,)).fetchone():
            short_id = generate_short_id()
            
        conn.execute('INSERT INTO urls (original_url, short_id) VALUES (?, ?)', (original_url, short_id))
        conn.commit()
    
    conn.close()
    
    short_url = request.host_url + short_id
    return jsonify({'short_url': short_url})

@app.route('/generate_qr', methods=['POST'])
def generate_qr():
    data = request.get_json()
    url = data.get('url')
    
    if not url:
        return jsonify({'error': 'URL is required'}), 400

    # Generate QR Code
    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(url)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black", back_color="white")

    img_io = io.BytesIO()
    img.save(img_io, 'PNG')
    img_io.seek(0)
    img_base64 = base64.b64encode(img_io.getvalue()).decode('utf-8')
    
    return jsonify({'qr_image': f"data:image/png;base64,{img_base64}"})

@app.route('/<short_id>')
def redirect_url(short_id):
    conn = get_db_connection()
    url_data = conn.execute('SELECT original_url FROM urls WHERE short_id = ?', (short_id,)).fetchone()
    conn.close()
    
    if url_data:
        return redirect(url_data['original_url'])
    else:
        return "URL not found", 404

if __name__ == '__main__':
    init_db()
    app.run(debug=True, host='0.0.0.0') # host='0.0.0.0' allows access from other devices on the same network