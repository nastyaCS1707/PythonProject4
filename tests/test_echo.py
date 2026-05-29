import requests

base_url_get = "https://postman-echo.com/get"
base_url_post = "https://postman-echo.com/post"

def test_get_request():
    response = requests.get(base_url_get)

    assert response.json()["url"] == base_url_get

def test_get_request_200():
    response = requests.get(base_url_get)
    assert response.status_code == 200

def test_get_with_query_params():
    params = {"key": "value"}
    response = requests.get(base_url_get, params=params)
    assert response.json()["args"] == params

def test_post_request():
    body = "value"
    response = requests.post(base_url_post, body)
    assert response.json()["data"] == body

def test_post_request_200():
    body = "new_data"
    response = requests.post(base_url_post, body)
    assert response.status_code == 200

def test_post_json_body():
    body = {'key': 'value'}
    response = requests.post(base_url_post, body)
    assert response.json()["form"] == body