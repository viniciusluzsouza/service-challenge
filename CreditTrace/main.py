from flask import Flask
from flask_cors import CORS

from controller.credit_trace_controller import creditTraceBP

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "SECRET"
app.register_blueprint(creditTraceBP)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002, debug=True)
