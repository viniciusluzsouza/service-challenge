from flask import Blueprint, jsonify, abort, request

from service.personal_registry_service import PersonalRegistryService

personalRegistryBP = Blueprint('personalRegistryBP', __name__)


# curl -i http://localhost:5000/personal_registry?cpf=12312312312
@personalRegistryBP.route('/personal_registry', methods=['GET'])
def getPersonalRegistry():
    cpf = request.args.get('cpf')

    if not cpf:
        return abort(400)

    try:
        personal_registry = PersonalRegistryService.getByCpf(cpf)
    except Exception as e:
        print("ERROR: %s" % str(e))
        return abort(500)

    return jsonify(personal_registry) if personal_registry else abort(404)
