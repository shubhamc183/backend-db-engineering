import requests

for i in range(0, 1000):
    requests.post(
        r'http://localhost:5000/?url=http://www.wikepedia.com/%s' % str(i))
