import main
import webtest


def test_get():
    app = webtest.TestApp(main.app)

    response = app.get('/')

    assert response.status_int == 200
assert response.body == 'Hello, World!'