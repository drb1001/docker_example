import os
import logging
from flask import Flask, render_template, jsonify


app = Flask(__name__)
app.logger.setLevel(logging.DEBUG)

@app.route('/', methods=['GET'])
def show_data():
    return render_template('template.html')


if __name__ == '__main__':

    port = int(os.environ.get("PORT", 8000))
    app.logger.info('Starting server on port {}'.format(port))
    app.run(host='0.0.0.0', port=port, debug=True)
