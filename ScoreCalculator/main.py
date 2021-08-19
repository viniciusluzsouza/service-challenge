from flask import Flask
from flask_cors import CORS

from controller.score_calculator_controller import score_calculator_bp

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "SECRET"
app.register_blueprint(score_calculator_bp)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5003, debug=True)
