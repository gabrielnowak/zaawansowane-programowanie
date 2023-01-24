import json
from flask import Flask, jsonify, request
from person_detection import detectPersons
appFlask = Flask(__name__)

@appFlask.route('/myApp/detectPersons')

def detect():
    img = request.args['image']
    dictionary = detectPersons(img)
    print(dictionary)
    return jsonify(dictionary)

appFlask.run(debug=True)