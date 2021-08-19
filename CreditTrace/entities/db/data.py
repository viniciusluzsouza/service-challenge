last_credit_query01 = {"institution": "Caixa", "good": "CASA", "value": 400000, "datetime": "2021-04-12T15:04:49"}
last_credit_query02 = {"institution": "Santander", "good": "CARRO", "value": 120000, "datetime": "2020-10-02T12:09:17"}
last_credit_query03 = {"institution": "Itau", "good": "EMPRESTIMO", "value": 10000, "datetime": "2021-01-23T16:43:31"}
last_credit_query04 = {"institution": "Nubank", "good": "EMPRESTIMO", "value": 21000, "datetime": "2019-03-28T19:13:55"}
last_credit_query05 = {"institution": "Itau", "good": "EMPRESTIMO", "value": 140000, "datetime": "2016-07-14T09:31:22"}

financial_movement01 = {"inputs": 30000, "outputs": 10000, "from": "2021-01-01T00:00:00", "to": "2021-06-30T23:59:59"}
financial_movement02 = {"inputs": 42000, "outputs": 60000, "from": "2021-01-01T00:00:00", "to": "2021-06-30T23:59:59"}
financial_movement03 = {"inputs": 65000, "outputs": 30000, "from": "2021-01-01T00:00:00", "to": "2021-06-30T23:59:59"}
financial_movement04 = {"inputs": 336000, "outputs": 100000, "from": "2021-01-01T00:00:00", "to": "2021-06-30T23:59:59"}
financial_movement05 = {"inputs": 70000, "outputs": 24000, "from": "2021-01-01T00:00:00", "to": "2021-06-30T23:59:59"}

last_credit_card_purchase01 = {"value": 250, "months": 1, "datetime": "2021-08-14T16:21:44"}
last_credit_card_purchase02 = {"value": 800, "months": 8, "datetime": "2021-08-10T21:20:36"}
last_credit_card_purchase03 = {"value": 56, "months": 1, "datetime": "2021-08-15T15:12:43"}
last_credit_card_purchase04 = {"value": 1400, "months": 3, "datetime": "2021-08-12T19:48:31"}
last_credit_card_purchase05 = {"value": 600, "months": 2, "datetime": "2021-08-13T22:52:10"}

DATA = [
    {"cpf": "12312312312", "last_credit_query": last_credit_query01, "financial_movement": financial_movement01,
     "last_credit_card_purchase": last_credit_card_purchase01},
    {"cpf": "32132132132", "last_credit_query": last_credit_query02, "financial_movement": financial_movement02,
     "last_credit_card_purchase": last_credit_card_purchase02},
    {"cpf": "45645645645", "last_credit_query": last_credit_query03, "financial_movement": financial_movement03,
     "last_credit_card_purchase": last_credit_card_purchase03},
    {"cpf": "65465465465", "last_credit_query": last_credit_query04, "financial_movement": financial_movement04,
     "last_credit_card_purchase": last_credit_card_purchase04},
    {"cpf": "78978978978", "last_credit_query": last_credit_query05, "financial_movement": financial_movement05,
     "last_credit_card_purchase": last_credit_card_purchase05},
]
