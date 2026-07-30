import os
import requests


class BaseAPI:
    base_url = os.getenv('BASE_URL')

    def get(self, endpoint):
        return requests.get(f'{self.base_url}/{endpoint}')

    def post(self, endpoint, headers, payload):
        return requests.post(
            f'{self.base_url}/{endpoint}',
            headers=headers,
            json=payload
        )
