#!/usr/bin/python3
"""Api"""

from api.v1.views import app_views
from os import getenv
from flask import Flask
from flask import jsonify
from flask_cors import CORS
from models import storage

app = Flask(__name__)
CORS(app, resources={r"/*": {"origins": "0.0.0.0"}})
app.url_map.strict_slashes = False
app.register_blueprint(app_views)


@app.teardown_appcontext
def app_teardown(exception):
    """Close section"""
    storage.close()

@app.errorhandler(404)
def notfound(error):
    """Handles 404 Errors"""
    return jsonify({"error": "Not found"}), 404

if __name__ == "__main__":
    app.run(
        host=getenv("HBNB_API_HOST", default="0.0.0.0"),
        port=getenv("HBNB_API_PORT", default=5000),
        threaded=True
    )
