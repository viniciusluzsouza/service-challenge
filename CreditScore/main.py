from flask import Flask
from flask_cors import CORS

from controller.credit_info_controller import creditInfoBP

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "SECRET"
app.register_blueprint(creditInfoBP)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5001, debug=True)
