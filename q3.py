import configparser
import json
import sqlite3
from flask import Flask, jsonify

CONFIG_FILE = 'config.ini'
DB_FILE = 'config_data.db'


def read_config(file_path):
    config = configparser.ConfigParser()
    try:
        config.read(file_path)
        if not config.sections():
            raise ValueError("Configuration file is empty or invalid format.")
        data = {section: dict(config.items(section)) for section in config.sections()}
        return data
    except FileNotFoundError:
        print(f"Error: Configuration file '{file_path}' not found.")
        return {}
    except Exception as e:
        print(f"Error reading configuration file: {e}")
        return {}


def save_to_db(data):
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS config (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                json_data TEXT NOT NULL
            )
        ''')
        cursor.execute('DELETE FROM config')  # Clear previous data
        cursor.execute('INSERT INTO config (json_data) VALUES (?)', (json.dumps(data),))
        conn.commit()
        conn.close()
    except Exception as e:
        print(f"Error saving to database: {e}")


def fetch_from_db():
    try:
        conn = sqlite3.connect(DB_FILE)
        cursor = conn.cursor()
        cursor.execute('SELECT json_data FROM config LIMIT 1')
        row = cursor.fetchone()
        conn.close()
        return json.loads(row[0]) if row else {}
    except Exception as e:
        print(f"Error fetching from database: {e}")
        return {}


# Flask API
app = Flask(__name__)


@app.route('/config', methods=['GET'])
def get_config():
    data = fetch_from_db()
    return jsonify(data)


if __name__ == '__main__':
    config_data = read_config(CONFIG_FILE)
    if config_data:
        print("Configuration File Parser Results:\n")
        for section, values in config_data.items():
            print(f"{section}:")
            for key, value in values.items():
                print(f"- {key}: {value}")
            print()
        save_to_db(config_data)
    app.run(debug=True)
