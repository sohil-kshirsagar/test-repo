"""
Mock helpers for testing - provides utilities to mock urllib.request calls.
"""


def mock_urlopen_factory(mock_responses):
    """
    Factory function to create a mock urlopen that returns predefined responses.
    
    Args:
        mock_responses: Dict mapping URLs to response data (as dicts/lists)
        
    Returns:
        A mock urlopen function
        
    Example:
        mock_responses = {
            'https://api.example.com/posts/1': {'id': 1, 'title': 'Test'},
            'https://api.example.com/posts/1/comments': [{'id': 1, 'body': 'Great!'}]
        }
        mock_urlopen = mock_urlopen_factory(mock_responses)
    """
    class MockResponse:
        def __init__(self, data):
            self.data = data
        
        def read(self):
            import json
            return json.dumps(self.data).encode('utf-8')
        
        def __enter__(self):
            return self
        
        def __exit__(self, *args):
            pass
    
    def mock_urlopen(url, timeout=None):
        if isinstance(url, str):
            request_url = url
        else:
            request_url = url.get_full_url()
        
        if request_url in mock_responses:
            return MockResponse(mock_responses[request_url])
        raise urllib.error.URLError(f"Mock URL not found: {request_url}")
    
    return mock_urlopen
