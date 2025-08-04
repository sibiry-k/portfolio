from http import HTTPStatus


class TestViews:
    def test_index(self, client):
        response = client.get('/')
        assert response.status_code == HTTPStatus.OK
