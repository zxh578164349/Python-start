import requests
def headers_to_dict(headers):
    """
    将字符串
    '''
    Host: mp.weixin.qq.com
    Connection: keep-alive
    Cache-Control: max-age=
    '''
    转换成字典对象
    {
        "Host": "mp.weixin.qq.com",
        "Connection": "keep-alive",
        "Cache-Control":"max-age="
    }
    :param headers: str
    :return: dict
    """
    headers = headers.split("\n")
    d_headers = dict()
    for h in headers:
        if h:
            k, v = h.split(":", 1)
            d_headers[k] = v.strip()
    return d_headers



# v0.1
def crawl():
    url = "https://mp.weixin.qq.com/mp/profile_ext?action=home&__biz=MjM5MzgyODQxMQ==&scene=124&devicetype=iOS11.2.6&version=16060320&lang=zh_CN&nettype=WIFI&a8scene=3&fontScale=100&pass_ticket=DueZI8gpcRn%2BY3QvA2omWqX%2BmU4MAsdzvuAK90DhQwhTlU25DVGIJPnMz4TrP8MU&wx_header=1" 
    headers="Host: mp.weixin.qq.com"
    "Cookie: devicetype=iOS11.2.6; lang=zh_CN; pass_ticket=DueZI8gpcRn+Y3QvA2omWqX+mU4MAsdzvuAK90DhQwhTlU25DVGIJPnMz4TrP8MU; version=16060320; wap_sid2=CJ/4w4wCElxobzVyYlN6YTBiOTBfM3F1QktnVUJsOC03WDEzS0VrMEZ3Sm9salppUlVwUzJGX3M3UlhxdE0wTVAzVWZiQnlINE1makFoMWRhTWU4Z3ZleXg2azJ3YklEQUFBfjCAzN3UBTgNQJVO; wxuin=563149855; rewardsn=; wxtokenkey=b83ea9a9eef675192f1a07b625572860a3f5c2b24028f401825dbccd94e6fbd6; pgv_info=ssid=s3293331095; pgv_pvid=1196723000"
    "X-WECHAT-KEY: c1eaea87f2f187535d304710d00a319489dfa8875c55effcd9faf1d86de5037080de59dd5ee3036e9c29e1d5a03e7b31713ef186ba462a54d893eb5ead50b6f42e98f02f448b17aeccc2f176f05b3031"
    "X-WECHAT-UIN: NTYzMTQ5ODU1"
    "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8"
    "User-Agent: Mozilla/5.0 (iPhone; CPU iPhone OS 11_2_6 like Mac OS X) AppleWebKit/604.5.6 (KHTML, like Gecko) Mobile/15D100 micromessage/6.6.3 NetType/WIFI Language/zh_CN"
    "Accept-Language: zh-cn"
    "Accept-Encoding: br, gzip, deflate"
    "Connection: keep-alive" 
    """  # 省略了
Host: mp.weixin.qq.com
Connection: keep-alive
Upgrade-Insecure-Requests: 1
    """
    headers = headers_to_dict(headers)
    response = requests.get(url, headers=headers, verify=False)
    print(response.text)

    with open("weixin_history.html", "w", encoding="utf-8") as f:
      f.write(response.text)

crawl()
