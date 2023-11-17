from flask import Flask, jsonify
from app.controller.SearchController import search_module

app = Flask(__name__)

app.register_blueprint(search_module)
app.register_blueprint()


# Run the Flask application
if __name__ == '__main__':
    app.run(debug=True)

