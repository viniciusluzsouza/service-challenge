class DebtDto(object):
    @staticmethod
    def getFrom(debt):
        return {
            "value": debt.value,
            "months": debt.months
        }


class PersonalRegistryDto(object):
    @staticmethod
    def getFrom(personal_registry):
        return {
            "cpf": personal_registry.cpf,
            "name": personal_registry.name,
            "address": personal_registry.address,
            "debts": [DebtDto.getFrom(debt) for debt in personal_registry.debts]
        }
