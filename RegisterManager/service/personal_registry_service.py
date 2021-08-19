from entities.base import Session
from entities.personal_registry import PersonalRegistry
from entities_dto.entities_dto import PersonalRegistryDto


class PersonalRegistryException(Exception):
    """ Exception to be raised when something goes wrong """


class PersonalRegistryService(object):
    @staticmethod
    def getByCpf(cpf):
        registry_dto = None
        session = None
        internal_error = False

        try:
            session = Session()
            personal_registry = session.query(PersonalRegistry).filter(PersonalRegistry.cpf == cpf).first()
            if personal_registry:
                registry_dto = PersonalRegistryDto.getFrom(personal_registry)

        except Exception as e:
            print("ERROR: %s" % str(e))
            internal_error = True
        finally:
            if session:
                session.close()

        if internal_error:
            raise PersonalRegistryException

        return registry_dto
