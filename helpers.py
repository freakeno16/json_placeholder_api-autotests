import random
from test_data.posts_data import posts_data

def get_random_post_title():
    return random.choice(posts_data["titles"])

def get_random_post_body():
    return random.choice(posts_data["bodies"])

def get_random_user_id():
    return random.choice(posts_data["ids"])