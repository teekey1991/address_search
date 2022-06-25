from urllib import response
import requests


#put = input("郵便番号を入力ください > ")
postal_code = ("0028061")

response = requests.get(f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}")

print(response)
#print(response.text)
dic = response.json()
print(dic)
