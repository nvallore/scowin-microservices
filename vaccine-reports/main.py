from flask import Flask, jsonify, abort
from flask_cors import CORS
from collections import defaultdict
import requests


app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def index():
    d = defaultdict(dict)
    studentRequest = requests.get('http://students-backend:8000/students')
    studentJson = studentRequest.json()

    vaccineRequest = requests.get('http://vaccination-backend:8001/student-vaccination')
    vaccineJson = vaccineRequest.json()

    for item in vaccineJson:
        d[item['student']].update(item)
    
    for item in studentJson:
        d[item['id']].update(item)

    print(d.values())

    
    return jsonify({
        'message': 'success',
        'report': list(d.values())
    })


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8003)