import requests


def get_redirect_url(url):
    # 重定向前的链接

    # 请求头，这里我设置了浏览器代理
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
        "Referer": "https://weibo.com/",
    }
    # 请求网页
    response = requests.get(url, headers=headers, timeout=30)
    # 返回重定向后的网址
    return response.url
