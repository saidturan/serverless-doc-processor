from src.processor import lambda_handler
from unittest.mock import patch

@patch("src.processor.s3_client")
def test_lambda_handler_success(mock_s3):
    mock_s3.head_object.return_value = {"ContentLength": 2048}
    mock_event = {"Records": [{"s3": {"bucket": {"name": "test-input-bucket"}, "object": {"key": "test_document.pdf"}}}]}
    result = lambda_handler(mock_event, None)
    assert result["statusCode"] == 200
    assert "2048 bytes" in result["body"]

def test_lambda_handler_invalid_event():
    result = lambda_handler({}, None)
    assert result["statusCode"] == 400
