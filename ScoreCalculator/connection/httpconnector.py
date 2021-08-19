import asyncio
import aiohttp


class HTTPConnector(object):
    def __init__(self, urls):
        self.urls = urls
        self.params = []

    def addParam(self, param, value):
        self.params.append((param, value))

    @staticmethod
    async def get(session, url, **kwargs):
        try:
            resp = await session.request('GET', url=url, **kwargs)
            data = await resp.json()
        except Exception:
            return resp, None

        return resp, data

    async def getAll(self):
        async with aiohttp.ClientSession() as session:
            tasks = []
            for url in self.urls:
                tasks.append(HTTPConnector.get(session, url, params=self.params))

            return await asyncio.gather(*tasks, return_exceptions=True)
