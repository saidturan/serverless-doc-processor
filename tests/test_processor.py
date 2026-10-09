from src.processor import lambda_handler

def test_lambda_handler():
    mock_event = {"Records": [{"s3": {"object": {"key": "test_document.pdf"}}}]}
    result = lambda_handler(mock_event, None)
    assert result["statusCode"] == 200
    assert "test_document.pdf" in result["body"]
