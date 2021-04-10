from flask import Flask

from flask import render_template
from flask import jsonify

import json

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('tickets_offers.html')

@app.route('/lista')
def load_data():

    # Opening JSON file
    f = open('test.json',)
    
    # returns JSON object as 
    # a dictionary
    data = json.load(f)
    
    # Iterating through the json
    # list
    
    # Closing file
    f.close()

    return jsonify(data)







if __name__ == "__main__":
    app.run(debug=True)
