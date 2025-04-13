from unittest.mock import patch, MagicMock

from producer import get_connection, publish


@patch("producer.BlockingConnection")
@patch("producer.ConnectionParameters")
def test_get_connection(mock_connection_parameters, mock_blocking_connection):
    get_connection()
    assert mock_connection_parameters.called
    assert mock_blocking_connection.called


@patch("producer.get_connection")
def test_publish(mock_get_connection):
    mocked_connection = MagicMock()
    mock_get_connection.return_value = mocked_connection
    publish(exchange='', queue='hello', body='Hello World')
    assert mock_get_connection.called
    assert mocked_connection.channel.called
    assert mocked_connection.channel.return_value.queue_declare.called
    assert mocked_connection.channel.return_value.basic_publish.called
