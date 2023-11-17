from flask import Flask, jsonify
from app.controller.SearchController import search_module

app = Flask(__name__)

app.register_blueprint(search_module)

# Run the Flask application
if __name__ == '_main_':
    app.run(debug=True)

