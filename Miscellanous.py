import requests

cookie = {"visit-month" : "February"}

response = requests.get("http://rahulshettyacademy.com", allow_redirects=False, cookies = cookie, timeout=10)
print(response.status_code)
print(response.history)

##httpbin cookies
response = requests.get("https://httpbin.org/cookies", cookies = cookie)
print(response.text)

se = requests.session()
se.cookies.update(cookie)

response = se.get("https://httpbin.org/cookies")
print(response.text)