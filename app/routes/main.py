from flask import Blueprint, render_template, request, jsonify
import json
import os
import random
from dotenv import load_dotenv

main = Blueprint('main', __name__)

load_dotenv()

SECRET_KEY = os.getenv("SECRET_KEY")
WAKE_FILE = os.getenv("WAKE_FILE")

@main.route('/')
def index():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'projects.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        projects = json.load(f)
    return render_template('index.html', projects=projects)

@main.route('/api/wake-trigger', methods=['POST'])
def trigger_wake():
    key = request.args.get('key')
    if key != SECRET_KEY:
        return jsonify({"error": "unauthorized"}), 403

    with open(WAKE_FILE, "w") as f:
        f.write("1")

    return jsonify({"status": "ok"})

@main.route('/api/wake-trigger', methods=['GET'])
def check_wake():
    if os.path.exists(WAKE_FILE):
        os.remove(WAKE_FILE)
        return jsonify({"wake": True})
    return jsonify({"wake": False})
