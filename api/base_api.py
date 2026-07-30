import os
import requests
from dotenv import load_dotenv


load_dotenv()

class BaseAPI:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL')

    def get(self, endpoint):
        return requests.get(f'{self.base_url}/{endpoint}')

    def post(self, endpoint, headers, payload):
        return requests.post(
            f'{self.base_url}/{endpoint}',
            headers=headers,
            json=payload
        )
