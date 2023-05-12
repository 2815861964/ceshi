import requests

headers = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.68"
}
response = requests.get('http://ysjdm8.com/acg/', headers)
text1 = response.text
text1 = text1.encode('utf-8')
text1 = str(text1, 'utf-8')
print(text1)
with open("./cs.html", "w", encoding='utf-8') as f:
    f.write(text1)
