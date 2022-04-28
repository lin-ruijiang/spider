import urllib.request
#
# response =urllib.request.urlopen("http://www.baidu.com")
# print(response.read().decode('utf-8'))
import urllib.error
import urllib.parse

# data = bytes(urllib.parse.urlencode({"hello":"world"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode("utf-8"))
#
# try:
#     response = urllib.request.urlopen("http://httpbin.org/post", timeout=0.1)
#     print(response.read().decode("utf-8"))
# except urllib.error.URLError as e:
#     print("time out!")


# response = urllib.request.urlopen("http://baidu.com")
# # print(response.status)
# # print(response.getheaders())
# print(response.getheaders("Server"))

url = "https://www.douban.com"
# url="http://httpbin.org/post"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:99.0) Gecko/20100101 Firefox/99.0"
}
data = bytes(urllib.parse.urlencode({"hello": "world"}), encoding="utf-8")
req = urllib.request.Request(url=url, data=data, headers=headers, method="POST")
response = urllib.request.urlopen(req)
print(response.read().decode("utf-8"))
