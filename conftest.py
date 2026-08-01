import random
import pytest
from dotenv import load_dotenv
from api.posts.posts_api import PostsAPI

load_dotenv()


@pytest.fixture()
def posts_api():
    return PostsAPI()


@pytest.fixture()
def get_post(posts_api):
    post = posts_api.get_post_by_id(random.randint(1, 100))

    yield post


@pytest.fixture()
def new_post(posts_api):
    post = posts_api.create_post()
    json_post = post.json()
    post_id = json_post["id"]

    yield post, post_id


@pytest.fixture()
def create_and_delete_post_after(posts_api):
    post = posts_api.create_post()
    post_id = post.json()["id"]

    yield post_id

    posts_api.delete_post_by_id(post_id)
