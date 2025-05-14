from flask import Blueprint, render_template
import json
import os
import random

main = Blueprint('main', __name__)

@main.route('/')
def index():
    json_path = os.path.join(os.path.dirname(__file__), '..', 'data', 'projects.json')
    with open(json_path, 'r', encoding='utf-8') as f:
        projects = json.load(f)
    return render_template('index.html', projects=projects)
