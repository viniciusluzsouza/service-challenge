from flask import Blueprint, jsonify, abort, request

from service.credit_info_service import CreditInfoService

creditInfoBP = Blueprint('creditInfoBP', __name__)


# curl -i http://localhost:5001/credit_info?cpf=12312312312
@creditInfoBP.route('/credit_info', methods=['GET'])
def getCreditInformation():
    cpf = request.args.get('cpf')

    if not cpf:
        return abort(400)

    try:
        credit_info = CreditInfoService.getByCpf(cpf)
    except Exception as e:
        print("ERROR: %s" % str(e))
        return abort(500)

    return jsonify(credit_info) if credit_info else abort(404)
