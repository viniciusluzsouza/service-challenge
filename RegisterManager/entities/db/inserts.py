from entities.personal_registry import PersonalRegistry
from entities.debt import Debt
from entities.base import Session


def insertDbRegistries():
    session = None
    try:
        session = Session()

        if session.query(Debt).first() is None:
            debt01 = Debt(15000, 12)
            debt02 = Debt(10000, 8)
            debt03 = Debt(200000, 250)
            debt04 = Debt(1000, 2)
            debt05 = Debt(13100, 18)
            debt06 = Debt(190, 2)
            debt07 = Debt(42131, 40)
            debt08 = Debt(3214, 6)
            debt09 = Debt(8321, 21)
            debt10 = Debt(400000, 300)

            personal_registry01 = PersonalRegistry("12312312312", "Joao Silva", "Rua do Joao, 150, Sao Paulo/SP",
                                                   [debt01, debt02])
            personal_registry02 = PersonalRegistry("32132132132", "Maria Matos", "Rua da Maria, 12, Rio de Janeiro/RJ",
                                                   [debt03, debt04])
            personal_registry03 = PersonalRegistry("45645645645", "Jose Souza", "Rua do Jose, 4, Florianopolis/SC",
                                                   [debt05, debt06])
            personal_registry04 = PersonalRegistry("65465465465", "Carla Rosa", "Rua da Carla, 1321, Goiania/GO",
                                                   [debt07, debt08])
            personal_registry05 = PersonalRegistry("78978978978", "Lucas Farias", "Rua do Lucas, 83, Salvador/BA",
                                                   [debt09, debt10])

            session.add(personal_registry01)
            session.add(personal_registry02)
            session.add(personal_registry03)
            session.add(personal_registry04)
            session.add(personal_registry05)

            session.commit()
        session.close()
    except Exception:
        print("Database info has not been inserted.")
    finally:
        if session is not None:
            session.close()
