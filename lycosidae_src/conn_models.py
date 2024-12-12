from urllib3 import PoolManager

# Define a custom PoolManager to prepend '/api/' to the URL
class CustomHTTPClient(PoolManager):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def urlopen(self, method, url, *args, **kwargs):
        # Add '/api/' prefix to the URL if it's localhost
        if url.startswith('http://localhost') or url.startswith('https://localhost'):
            url = url.replace('://localhost', '://localhost/api', 1)
        return super().urlopen(method, url, *args, **kwargs)