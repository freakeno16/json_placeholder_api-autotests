import requests
from api.base_api import BaseAPI


class PostsAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = '/posts'

    def get_all_posts(self):
        # return requests.get(f'{self.base_url}{self.endpoint}')
        return self.get(self.endpoint)