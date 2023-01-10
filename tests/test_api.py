def test_response(connection):
    assert connection.status_code == 200


def test_text(connection):
    assert 'btc' in connection.text



