from flask import Flask
from flask_cors import CORS

from controller.personal_registry_controller import personalRegistryBP
from entities.debt import Debt
from entities.personal_registry import PersonalRegistry
from entities.base import Base, engine
from entities.db.inserts import insertDbRegistries

app = Flask(__name__)
CORS(app)
app.config['SECRET_KEY'] = "SECRET"
app.register_blueprint(personalRegistryBP)

if __name__ == "__main__":
    Base.metadata.create_all(engine)
    insertDbRegistries()
    app.run(host='0.0.0.0', port=5005, debug=True)
