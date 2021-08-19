from entities.db.data import DATA


class PersonalCreditTrace(object):

    @staticmethod
    def createByCpf(cpf):
        info = next((d for d in DATA if d["cpf"] == cpf), None)
        if info:
            return PersonalCreditTrace(info)
        else:
            return None

    def _setInformation(self):
        self.cpf = self.personalCreditTraceData.get("cpf")
        self.last_credit_query = self.personalCreditTraceData.get("last_credit_query")
        self.financial_movement = self.personalCreditTraceData.get("financial_movement")
        self.last_credit_card_purchase = self.personalCreditTraceData.get("last_credit_card_purchase")

    def __init__(self, personal_credit_trace_data):
        self.personalCreditTraceData = personal_credit_trace_data
        self._setInformation()

    def getInfo(self):
        return self.personalCreditTraceData
