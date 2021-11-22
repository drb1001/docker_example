import os
import logging
from flask import Flask, request, jsonify
from random import randint
from flask_cors import CORS


app = Flask(__name__)
CORS(app)

app.logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET'])
def api():
    n_input = request.args.get('n', "", type=int)
    app.logger.info('n_input: {}'.format(n_input))
    if n_input not in range(1,10):
        n_input = 3
    data = [randint(0,10) for _ in range(n_input)]
    app.logger.info("data: {}".format(data))
    return jsonify(data)


if __name__ == '__main__':
    port = int(os.environ.get("PORT", 8001))
    app.logger.info('Starting server on port {}'.format(port))
    app.run(host='0.0.0.0', port=port, debug=True)
