from entities.personal_credit_trace import PersonalCreditTrace


class CreditTraceService(object):
    @staticmethod
    def getByCpf(cpf):
        credit_trace_dto = None

        credit_trace_obj = PersonalCreditTrace.createByCpf(cpf)
        if credit_trace_obj:
            credit_trace_dto = credit_trace_obj.getInfo()

        return credit_trace_dto
