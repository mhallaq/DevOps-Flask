from flask import Flask, request, jsonify, Response

from random import randint

app = Flask(__name__)

@app.route('/latitude', methods=['GET'])
def get_lat():
    lat=randint(0, 90)
    return Response(str(lat), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5003)