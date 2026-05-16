import sender_stand_request
import data

def get_token():
    user_body = data.user_body
    resp_user = sender_stand_request.post_new_user(user_body)
    print(resp_user.json())

    return resp_user.json()["authToken"]

def cambiar_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_test(body):
    token = get_token()
    response = sender_stand_request.post_new_kit(body, token)
    assert response.status_code == 201
    assert response.json()["name"] == body["name"]

def negative_test(body):
    token = get_token()
    response = sender_stand_request.post_new_kit(body, token)
    assert response.status_code == 400


def test_1_char():
    nuevo_body = cambiar_kit_body("a")
    positive_test(nuevo_body)

def test_511_chars():
    nuevo_body = cambiar_kit_body("a" * 512)
    positive_test(nuevo_body)

def test_empty_name():
    negative_test("")

def test_512_chars():
    negative_test("a" * 512)

def test_special_chars():
    nuevo_body = cambiar_kit_body("N%@")
    positive_test(nuevo_body)

def test_spaces():
    nuevo_body = cambiar_kit_body(" A Aaa")
    positive_test(nuevo_body)

def test_numbers():
    nuevo_body = cambiar_kit_body("123")
    positive_test(nuevo_body)

def test_no_name():
    token = get_token()
    response = sender_stand_request.post_new_kit({}, token)
    assert response.status_code == 400

def test_wrong_type():
    nuevo_body = cambiar_kit_body(123)
    negative_test(nuevo_body)
