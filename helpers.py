import random
from test_data.posts_data import posts_data

def get_random_post_title():
    return random.choice(posts_data['titles'])

def get_random_post_body():
    return random.choice(posts_data['body'])

def get_random_post_id():
    return random.choice(posts_data['id'])