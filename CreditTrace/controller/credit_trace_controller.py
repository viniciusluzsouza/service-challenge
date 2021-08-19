from flask import Blueprint, jsonify, abort, request

from service.credit_trace_service import CreditTraceService

creditTraceBP = Blueprint('creditTraceBP', __name__)


# curl -i http://localhost:5002/credit_trace?cpf=12312312312
@creditTraceBP.route('/credit_trace', methods=['GET'])
def getCreditTrace():
    cpf = request.args.get('cpf')

    if not cpf:
        return abort(400)

    try:
        credit_trace = CreditTraceService.getByCpf(cpf)
    except Exception as e:
        print("ERROR: %s" % str(e))
        return abort(500)

    return jsonify(credit_trace) if credit_trace else abort(404)
