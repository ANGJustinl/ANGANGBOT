import httpx
from httpx import Headers


async def get_redirect_url(url: str, headers: Headers = None) -> str:
    """获取重定向后的URL (纯 async)"""
    if headers is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Referer": "https://weibo.com/",
        }
    async with httpx.AsyncClient(follow_redirects=True, timeout=30, verify=False) as client:
        response = await client.get(url, headers=headers)
        return str(response.url)


async def get_msgurl(url: str, headers: Headers = None) -> bytes:
    """获取图片内容 (async)"""
    if headers is None:
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36",
            "Referer": "https://weibo.com/",
        }
    async with httpx.AsyncClient(timeout=5, verify=False) as client:
        resp = await client.get(url, headers=headers)
        return resp.content


async def get_daily_image(url, token) -> str:
    async with httpx.AsyncClient(verify=False, timeout=None) as client:
        resp = await client.post(
            url,
            data={"token": token},
        )
        msg_raw = resp.json()["data"]
        msg_url = msg_raw["image"]

    return msg_url
