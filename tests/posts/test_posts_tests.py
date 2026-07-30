def test_get_all_posts(posts_api):
    response = posts_api.get_all_posts()
    posts_api.assert_status_code(response, 200)

