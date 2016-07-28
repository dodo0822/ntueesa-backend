#!flask/bin/python
from flask import Flask
from flask import jsonify
import json

app = Flask(__name__, static_url_path='')

@app.route('/api')
def index():
    return "API Server GJGJMI"

@app.route('/api/course', methods=['GET'])
def get_course():
    with open('api/course.json') as data_file:
            course_data = json.load(data_file)
    return jsonify(results = course_data)
    #return app.send_static_file('api/course.json')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=7122, debug=True)
