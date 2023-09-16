import asyncio
import httpx

async def get_msg(url,token):
   async with httpx.AsyncClient(verify=False, timeout=None) as client:
    resp = await client.post(
      url,
      data={'token':token
      },
    )
    msg_raw = resp.json()['data']
    msg_url =  msg_raw['image']\

    return msg_url

async def get_msg2(url):
   async with httpx.AsyncClient(verify=False, timeout=None) as client:
    resp = await client.post(
      url,
    )
    msg_raw = resp.json()['data']
    msg_url =  msg_raw['urls']['original']
    return msg_url