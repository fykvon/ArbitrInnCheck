import traceback

from flask import Flask, request, jsonify
from utils import arbitr_check
from werkzeug.exceptions import HTTPException

app = Flask(__name__)


@app.route('/arbitr', methods=['GET'])
def get_info():
    inn = request.args.get('arbitr_inn')
    result = arbitr_check(inn)
    return jsonify(result)


@app.errorhandler(HTTPException)
def httr_error(exc):
    if exc.code in (400, 401, 403, 404):
        return jsonify({'error': f'{exc.name}: {exc.description}'}), exc.code


@app.errorhandler(500)
def httr_error(exc):
    return jsonify({'error': f'{type(exc.original_exeption).name}: {str(exc.original_exeption)}',
                    'traceback': traceback.format_exc()}), exc.code


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8001)
