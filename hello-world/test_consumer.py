from unittest.mock import MagicMock

from consumer import on_message_callback


def test_on_message_callback():
    mock_channel = MagicMock()
    mock_method = MagicMock()
    on_message_callback(mock_channel, mock_method, MagicMock(), 'Hello World'.encode())
    assert mock_channel.basic_ack.called
    call_args = mock_channel.basic_ack.call_args
    kwargs = call_args.kwargs
    assert kwargs['delivery_tag'] == mock_method.delivery_tag
