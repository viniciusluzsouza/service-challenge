import asyncio

from connection.httpconnector import HTTPConnector

from datetime import datetime

# TODO set as an environment variable
CREDIT_INFO_URL = "http://credit-score:5001/credit_info"
CREDIT_TRACE_URL = "http://credit-trace:5002/credit_trace"
#CREDIT_INFO_URL = "http://localhost:5001/credit_info"
#CREDIT_TRACE_URL = "http://localhost:5002/credit_trace"
URLS = [CREDIT_INFO_URL, CREDIT_TRACE_URL]


class NotFoundException(Exception):
    '''Raised when the resource is not found on other services'''


class RequestErrorException(Exception):
    '''Raised when some error has happened on other services'''


class CreditCalcService(object):
    def __init__(self, cpf, credit_info=None, rate=0):
        self.cpf = cpf
        self.credit_info = credit_info
        self.rate = rate

    def _get_oldest_in_years(self, dates):
        years = 0
        dates_obj = []

        for date in dates:
            try:
                dates_obj.append(datetime.strptime(date, '%Y-%m-%d'))
            except Exception:
                pass

        if len(dates_obj):
            years = int((datetime.now() - max(dates_obj)).days / 365)

        return years

    def _fix_rate_value(self, value):
        if value > 100:
            return 100
        elif value < 0:
            return 0
        else:
            return value

    def _prepare_credit_info(self):
        prepared_credit_info = {}
        for cred_info in self.credit_info:
            prepared_credit_info.update(cred_info)

        self.credit_info = prepared_credit_info

    # Generate a score from 0 to 1000
    def _calc(self):
        if not self.credit_info:
            return 0

        self._prepare_credit_info()
        incomes_since = list(filter(lambda i: i, [i.get("since", None) for i in self.credit_info.get('incomes', [])]))
        income_rate = 20 * self._get_oldest_in_years(incomes_since)
        income_rate = self._fix_rate_value(income_rate) * 2  # Fix value and set weight

        goods_value = 0
        goods_value += sum([good.get("value", 0) / 100000 for good in self.credit_info.get('goods', [])])
        goods_rate = 10 * goods_value
        goods_rate = self._fix_rate_value(goods_rate) * 2  # Fix value and set weight

        financial_movement_rate = 0
        financial_movement = self.credit_info.get('financial_movement', None)
        if financial_movement:
            financial_movement_rate = (1 - (
                        financial_movement.get('outputs', 0) / financial_movement.get('inputs', 1))) * 100
        financial_movement_rate = self._fix_rate_value(financial_movement_rate) * 3  # Fix value and set weight

        last_purchase_rate = 0
        last_purchase = self.credit_info.get('last_credit_card_purchase', None)
        if last_purchase:
            last_purchase_rate = 100 - (10 * (max(last_purchase.get("months", 0), 1) - 1))
        last_purchase_rate = self._fix_rate_value(last_purchase_rate) * 1  # Fix value and set weight

        last_credit_rate = 0
        last_credit = self.credit_info.get('last_credit_query', None)
        if last_credit:
            last_credit_rate = 20 if last_credit.get('good') == 'EMPRESTIMO' else 100
            last_credit_rate -= 20 if last_credit.get('value') > 100000 else 0
        last_credit_rate = self._fix_rate_value(last_credit_rate) * 1  # Fix value and set weight

        age_rate = 2 * self.credit_info.get('age', 0)
        age_rate = self._fix_rate_value(age_rate) * 1  # Fix value and set weight

        self.rate = income_rate + goods_rate + financial_movement_rate + last_purchase_rate + last_credit_rate + age_rate

    def _getHttpResponse(self, resp):
        if not len(resp) or not len(resp[0]):
            raise Exception

        http_resps = [r[0] for r in resp]
        for hr in http_resps:
            if hr.status == 404:
                raise NotFoundException
            if hr.status != 200:
                raise RequestErrorException("Could not get data to calculate")

        resp_jsons = [r[1] for r in resp]
        return resp_jsons

    def getCalcDto(self):
        return {"cpf": self.cpf, "rate": self.rate, "data": self.credit_info}

    def calculate(self):
        http_connector = HTTPConnector(URLS)
        http_connector.addParam("cpf", self.cpf)

        self.credit_info = self._getHttpResponse(asyncio.run(http_connector.getAll()))
        if not self.credit_info:
            return None

        self._calc()
        return self.getCalcDto()
