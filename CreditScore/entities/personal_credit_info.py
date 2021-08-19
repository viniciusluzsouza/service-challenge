import json

DB_FILE = "./entities/db/data.json"


class PersonalCreditInfo(object):

    @staticmethod
    def createByCpf(cpf):
        data = []
        try:
            with open(DB_FILE, 'r') as f:
                data = json.load(f)
        except Exception as e:
            print("Data could not be loaded: %s" % str(e))

        info = next((d for d in data if d["cpf"] == cpf), None)
        if info:
            return PersonalCreditInfo(info)
        else:
            return None

    def _setInformation(self):
        self.cpf = self.personalCreditInformation.get("cpf")
        self.age = self.personalCreditInformation.get("age")
        self.address = self.personalCreditInformation.get("address")
        self.incomes = self.personalCreditInformation.get("incomes")
        self.goods = self.personalCreditInformation.get("goods")

    def __init__(self, personal_credit_information):
        self.personalCreditInformation = personal_credit_information
        self._setInformation()

    def getInfo(self):
        return self.personalCreditInformation
