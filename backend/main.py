from flask import Flask, request, jsonify
from flask_cors import CORS
from datetime import datetime, timedelta
import os, psycopg2
from psycopg2.extras import RealDictCursor

app = Flask(__name__)
CORS(app)

def get_db_connection():
    return psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'beauty_db'),
        user=os.environ.get('DB_USER', 'admin'),
        password=os.environ.get('DB_PASSWORD', 'beauty123') # Uskladi sa compose fajlom
    )

@app.route('/calculate', methods=['POST'])
def calculate():
    data = request.json
    try:
        otvoren_dt = datetime.strptime(data['datum'], '%d.%m.%Y')
        istek_dt = otvoren_dt + timedelta(days=int(data['rucni_rok'])*30)
        
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO kalkulacije (brend, proizvod, datum_otvaranja, datum_isteka) VALUES (%s, %s, %s, %s)",
            (data['brend'], data['proizvod'], otvoren_dt.date(), istek_dt.date())
        )
        conn.commit()
        cur.close()
        conn.close()
        return jsonify({"status": "success", "istice_datuma": istek_dt.strftime('%d.%m.%Y')})
    except Exception as e:
        return jsonify({"status": "error", "message": str(e)}), 400

@app.route('/history', methods=['GET'])
def history():
    conn = get_db_connection()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM kalkulacije ORDER BY datum_isteka ASC")
    rows = cur.fetchall()
    cur.close()
    conn.close()
    
    danas = datetime.now().date()
    return jsonify([{
        "id": r['id'], "brend": r['brend'], "proizvod": r['proizvod'],
        "otvoreno": r['datum_otvaranja'].strftime('%d.%m.%Y'),
        "istek": r['datum_isteka'].strftime('%d.%m.%Y'),
        "dana_do": (r['datum_isteka'] - danas).days
    } for r in rows])

@app.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    conn = get_db_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM kalkulacije WHERE id = %s", (id,))
    conn.commit()
    cur.close()
    conn.close()
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)