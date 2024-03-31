#!/usr/bin/python3

"""Api"""
from os import getenv
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from models import storage
from api.v1.views import app_views

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)

@app.errorhandler(404)
def notfound(error):
    """404 Error  Not found"""
    return jsonify({"error": "Not found"}), 404

@app.teardown_appcontext
def app_teardown(exception):
    """Closes the storage session"""
    storage.close()

if __name__ == "__main__":
    app.run(
        host=getenv("HBNB_API_HOST", default="0.0.0.0"),
        port=getenv("HBNB_API_PORT", default=5000),
        threaded=True
    )
