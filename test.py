from api import app

def test_hello():
    response = app.test_client().get('/')

    assert response.status_code == 200
    assert response.data == 'Hello World, it\'s wonderful top see you!'
