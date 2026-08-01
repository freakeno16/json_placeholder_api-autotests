def test_get_all_posts(posts_api):
    response = posts_api.get_all_posts()
    posts_api.check_status_code_is(response, 200)

def test_get_post_by_id(posts_api):
    response = posts_api.get_post_by_id()
    posts_api.check_status_code_is(response, 200)

def test_create_post(posts_api):
    response = posts_api.create_post()
    posts_api.check_status_code_is(response, 201)

def test_delete_post_by_id(posts_api, new_post):
    response = posts_api.delete_post_by_id(new_post)
    posts_api.check_status_code_is(response, 200)
    posts_api.check_body_is_empty(response)

    deleted_post = posts_api.get_post_by_id(new_post)
    posts_api.check_status_code_is(deleted_post, 404)

def test_update_post(posts_api, get_post):
    response = posts_api.update_post(get_post)
    posts_api.check_status_code_is(response, 200)
    posts_api.check_post_title_is_updated(response, get_post)
