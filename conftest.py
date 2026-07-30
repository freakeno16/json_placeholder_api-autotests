import pytest
from api.posts.posts_api import PostsAPI


@pytest.fixture()
def posts_api():
    return PostsAPI()
