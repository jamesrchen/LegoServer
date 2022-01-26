from flask import Flask, request

from brick_utils import jsonToBricks
from brick_utils import saveBricks

app = Flask(__name__)

@app.after_request
def after_request(response):
    header = response.headers
    header['Access-Control-Allow-Origin'] = '*'
    header['Access-Control-Allow-Headers'] = 'Content-Type'
    return response

@app.route('/api/upload', methods=['POST'])
def upload():
    print(request.get_json())
    print(jsonToBricks(request.get_json()))
    saveBricks(jsonToBricks(request.get_json()))
    return request.data

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='8081', debug=True)