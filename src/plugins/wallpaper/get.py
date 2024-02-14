import asyncio
from socket import timeout
import httpx
import base64


async def get_msgurl(url):
    async with httpx.AsyncClient(verify=False, timeout=None) as client:
        resp = await client.get(
            url, headers={"Referer": "https://weibo.com/"}, timeout=30
        )
        page = resp.content
        # res = re.compile(r'src="(http.+?.jpg)"')
        # reg = re.findall(res, page)
        # print(reg)
        return page
