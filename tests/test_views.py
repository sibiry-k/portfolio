class TestViews:
    def test_index_page(self, client):
        response = client.get('/')
        assert response.status_code == 200
