import requests

r = requests.get('https://api.github.com/events')

print(" json body", r.json())