# main.py
import requests

response = requests.get("https://www.news.com")
print(f"Status Code: {response.status_code}")
print(f"Content Length: {len(response.text)} bytes")
