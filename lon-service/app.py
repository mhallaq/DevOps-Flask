from flask import Flask, request, jsonify, Response

from random import randint

app = Flask(__name__)

@app.route('/longitude', methods=['GET'])
def get_lon():
    lon=randint(0, 180)
    print(lon)
    return Response(str(lon), mimetype='text/plain')


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0',port=5002)