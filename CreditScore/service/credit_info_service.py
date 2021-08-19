from entities.personal_credit_info import PersonalCreditInfo


class CreditInfoService(object):
    @staticmethod
    def getByCpf(cpf):
        credit_info_dto = None

        credit_info_obj = PersonalCreditInfo.createByCpf(cpf)
        if credit_info_obj:
            credit_info_dto = credit_info_obj.getInfo()

        return credit_info_dto
