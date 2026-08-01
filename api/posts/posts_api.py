from api.base_api import BaseAPI
import helpers


class PostsAPI(BaseAPI):
    def __init__(self):
        super().__init__()
        self.endpoint = '/posts'

    def get_all_posts(self):
        return self.get(self.endpoint)

    def get_post_by_id(self, post_id):
        return self.get(f'{self.endpoint}/{post_id}')

    def create_post(self):
        headers = {
            "Content-Type": "application/json; charset=UTF-8"
        }

        payload = {
            "title": helpers.get_random_post_title(),
            "body": helpers.get_random_post_body(),
            "userId": helpers.get_random_user_id()
        }

        post = self.post(self.endpoint, headers=headers, payload=payload)

        return post

    def update_post(self, original_post):
        headers = {
            "Content-Type": "application/json; charset=UTF-8"
        }

        payload = {
            "title": helpers.get_random_post_title(),
            "body": helpers.get_random_post_body(),
            "userId": helpers.get_random_user_id()
        }

        post_id = original_post.json()['id']
        post = self.put(f'{self.endpoint}/{post_id}', headers=headers, payload=payload)
        return post

    def delete_post_by_id(self, post_id):
        post = self.delete(f'{self.endpoint}/', post_id)

        return post

    def check_post_title_is_updated(self, response, original_post):
        original_post_title = original_post.json()['title']
        new_post_title = response.json()['title']

        assert original_post_title != new_post_title, f'''
        Скорее всего title не изменился:
        Старый title: {original_post_title}
        Новый title: {new_post_title}
        '''