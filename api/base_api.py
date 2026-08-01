import os
import requests
from dotenv import load_dotenv

load_dotenv()

class BaseAPI:
    def __init__(self):
        self.base_url = os.getenv('BASE_URL')

    def get(self, endpoint):
        return requests.get(f'{self.base_url}{endpoint}')

    def post(self, endpoint, headers, payload):
        return requests.post(
            f'{self.base_url}{endpoint}',
            headers=headers,
            json=payload
        )

    def put(self, endpoint, headers, payload):
        return requests.put(
            f'{self.base_url}{endpoint}',
            headers=headers,
            json=payload
        )

    def delete(self, endpoint, post_id):
        return requests.delete(f'{self.base_url}{endpoint}/{post_id}')

    def check_status_code_is(self, response, expected_status_code):
        assert response.status_code == expected_status_code, f'''
        'Ожидали: {expected_status_code}',
        'Получили: {response.status_code}'
        '''

    def check_body_is_empty(self, response):
        assert response.json() == {}
