from app import geraCurriculo
from flask_cors import CORS, cross_origin
from flask import Flask, request, abort, jsonify, send_from_directory

def create_app():
    app = Flask(__name__)
    CORS(app)

    @app.route('/cv', methods=['POST'])
    def cv_generator():
        if not request.json:
            abort(400)

        fileName = geraCurriculo(request.json)

        return send_from_directory('/home/charles/cv-generator', fileName)

    return app
