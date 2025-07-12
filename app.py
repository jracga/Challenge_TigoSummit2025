from flask import Flask
from routes.mock_routes import mock_blueprint

app = Flask(__name__)
app.register_blueprint(mock_blueprint)

if __name__ == "__main__":
    app.run(debug=True)
