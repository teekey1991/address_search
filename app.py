import requests


# postal_code = input("郵便番号を入力ください > ")
postal_code = "0287111"

response = requests.get(
    f"https://zipcloud.ibsnet.co.jp/api/search?zipcode={postal_code}"
)

print(response)
# print(response.text)  #テキスト
dic = response.json() #パース
#print(dic)
pref_name = dic['results'][0]['address1'] #都道府県
city_name = dic['results'][0]['address2'] #市区
town_name = dic['results'][0]['address3'] #町村

print(f"{pref_name}{city_name}{town_name}")