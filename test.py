import requests
import json

url = "http://127.0.0.1:8000/predict"

data = {
    "text": "Cuộc sống không lường trước điều gì, tình yêu có thể đến rồi đi."
}
res = requests.post(url, json=data)
print("\n--- Test 1 ---")
print("Request:")
print(json.dumps(data, indent=2, ensure_ascii=False))
print("Status:", res.status_code)
print("Response:")
print(json.dumps(res.json(), indent=2, ensure_ascii=False))


data = {
    "text": "Thế giới, hãy tốt bụng với cô ấy."
}
res = requests.post(url, json=data)
print("\n--- Test 2 ---")
print("Request:")
print(json.dumps(data, indent=2, ensure_ascii=False))
print("Status:", res.status_code)
print("Response:")
print(json.dumps(res.json(), indent=2, ensure_ascii=False))


data = {"text": ""}
res = requests.post(url, json=data)
print("\n--- Test 3 ---")
print("Request:")
print(json.dumps(data, indent=2, ensure_ascii=False))
print("Status:", res.status_code)
print("Response:")
print(json.dumps(res.json(), indent=2, ensure_ascii=False))


data = {"text": 123}
res = requests.post(url, json=data)
print("\n--- Test 4 ---")
print("Request:")
print(json.dumps(data, indent=2, ensure_ascii=False))
print("Status:", res.status_code)
print("Response:")
print(json.dumps(res.json(), indent=2, ensure_ascii=False))