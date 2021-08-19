from flask import Blueprint, jsonify, abort, request

from service.credit_calc_service import CreditCalcService, NotFoundException, RequestErrorException

score_calculator_bp = Blueprint('score_calculator_bp', __name__)


# curl -i http://localhost:5003/credit_calc?cpf=12312312312
@score_calculator_bp.route('/credit_calc', methods=['GET'])
def runCreditCalc():
    cpf = request.args.get('cpf')

    if not cpf:
        return abort(400)

    try:
        credit_calc_service = CreditCalcService(cpf)
        credit_calc_result = credit_calc_service.calculate()
    except NotFoundException:
        return abort(404)
    except Exception as e:
        print("ERROR: %s" % str(e))
        return abort(500)

    return jsonify(credit_calc_result) if credit_calc_result else abort(404)
