import os
import asyncio
from datetime import datetime

from nonebot import on_command, on_regex, require
from nonebot.log import logger
from nonebot.typing import T_State
from nonebot.matcher import Matcher
from nonebot.plugin import PluginMetadata
from nonebot.params import ArgPlainText, CommandArg
from nonebot.adapters.onebot.v11 import Bot, Message, Event, MessageSegment, MessageEvent

from .utils import get_redirect_url, get_msgurl
from .scheduler import get_daily_image_scheduler
from .limiter import FreqLimiter

require("nonebot_plugin_apscheduler")
from nonebot_plugin_apscheduler import scheduler


__plugin_meta__ = PluginMetadata(
    name="壁纸鉴赏",
    description="壁纸鉴赏",
    usage="壁纸",
    extra={
        "menu_data": [
            {
                "func": "壁纸",
                "trigger_method": "关键词命令",
                "trigger_condition": "wp",
                "brief_des": "壁纸",
                "detail_des": "随机出壁纸",
            },
            {
                "func": "运气检测",
                "trigger_method": "关键词命令",
                "trigger_condition": "wpwp",
                "brief_des": "打开随机出一张图70%穿衣服，不漏18%穿衣服，少漏8%穿游装2.8%穿游装,少漏1%穿游装,多漏0.2%不穿非酋还会刷出来风景图",
                "detail_des": "打开随机出一张图70%穿衣服，不漏18%穿衣服，少漏8%穿游装2.8%穿游装,少漏1%穿游装,多漏0.2%不穿非酋还会刷出来风景图",
            },
        ],
        "menu_template": "default",
    },
)
limiter_default = FreqLimiter(60)
limiter_loong = FreqLimiter(114514)

scheduler.add_job(get_daily_image_scheduler, "cron", hour=8, misfire_grace_time=600)
asyncio.run(get_daily_image_scheduler())

get_random_wallpaper = on_command("壁纸", aliases={"wp"}, priority=10, block=True)
get_random_wallpapers = on_command("多张壁纸", aliases={"wps"}, priority=10, block=True)
re = on_command(
    "运气检测", aliases={"luck", "随机壁纸", "wpwp"}, priority=10, block=True
)
food = on_command("美食", aliases={"food"}, priority=10, block=True)
daily = on_command("每日新闻", aliases={"news"}, priority=10, block=True)
msn = on_command("msn", priority=5, block=True)
sese = on_command("sese")
mature = on_command("mature", aliases={"r18roll1"}, priority=5, block=True)
m2 = on_command("mature2", aliases={"r18roll2"}, priority=5, block=True)


@get_random_wallpaper.handle()
async def _(matcher: Matcher, event: MessageEvent):
    user_id = event.user_id
    if not limiter_default.check(user_id):
        left_time = limiter_default.left_time(user_id)
        await matcher.finish(f"我知道你急了.但是你先别急,cd还有{left_time}秒")
        return

    limiter_default.start_cd(user_id)
    url = await get_redirect_url(
        "https://moe.anosu.top/img"
    )  # 确保 get_redirect_url 是 async
    try:
        await get_random_wallpaper.send(
            "您点的图来了{}".format(url) + MessageSegment.image(file=url, cache=False),
            at_sender=True,
        )
    except Exception as e:
        await get_random_wallpaper.finish(
            "tx风控了...", at_sender=True
        )
    else:
        await get_random_wallpaper.finish()

@get_random_wallpapers.handle()
async def _(matcher: Matcher, event: MessageEvent):
    user_id = event.user_id
    if not limiter_default.check(user_id):
        left_time = limiter_default.left_time(user_id)
        await matcher.finish(f"我知道你急了.但是你先别急,cd还有{left_time}秒")
        return

    limiter_default.start_cd(user_id)

@get_random_wallpapers.got("number", prompt="请输入你想要获取的图片数量")
async def get_random_wallpapers_number(bot: Bot, event: MessageEvent, number: int = ArgPlainText()):
    await get_random_wallpapers.send(f"图片正在获取中，请稍等...")
    try:
        image_list = []
        msg_list = []
        for i in range(int(number)):
            url = await get_redirect_url("https://moe.anosu.top/img")
            base64_data = await get_msgurl(url)
            await asyncio.sleep(0.5)
            image_list.append((base64_data, url))

        msg_list.append("获取的图片如下：\n")
        for base64_data, url in image_list:
            msg_list.append(
                    Message(f"图片链接： {url}\n")
                    + MessageSegment.image(base64_data, cache=False)
                )
            msgs = [
                    {
                        "type": "node",
                        "data": {
                            "name": "setu-bot",
                            "uin": bot.self_id,
                            "content": msg,
                        },
                    }
                    for msg in msg_list
                ]
            await asyncio.sleep(0.5)
        await bot.call_api("send_group_forward_msg", group_id=event.group_id, messages=msgs)
    except Exception as e:
        await get_random_wallpapers.finish(f"tx 风控了... {str(e)}")
    else:
        await get_random_wallpapers.finish()

@mature.handle()
async def _(matcher: Matcher, event: MessageEvent, bot: Bot):
    await mature.finish("暂时关闭")
'''    user_id = event.user_id
    # if not limiter.check(user_id):
    #    left_time = limiter.left_time(user_id)
    #    await matcher.finish(f'我知道你急了.但是你先别急,一天一次')
    #    return
    setu_msg_id = []
    limiter.start_cd(user_id)
    # url = 'https://blog.angforever.top/r18roll/roll.html'
    url = get_redirect_url("https://moe.jitsu.top/r18")
    test_xml = f"""<?xml version="1.0" encoding="utf-8"?><msg flag='4' serviceID='1' brief='[图文消息]' templateID='1' action='plugin' url='{url}'><item layout='5'><picture cover='https://upyuncloud.angforever.top/uploads%2F2023%2F05%2F15%2FSsBxLvKe_avatar.png?'/></item><item layout='0' /><item layout='0'><summary size="40" color="#ff0000">📣 看看你的运气</summary></item>
    <item><hr></hr><summary size="32" color="#ff0000">Test</summary></item><source name="昂昂bot" icon="" url="https://blog.angforever.top/2023/01/06/ANGANGBOT1/"/></msg>"""
    setu_msg_id.append((await mature.send(MessageSegment.xml(test_xml)))["message_id"])
    # await wp.send("您点的图来了{}".format(url), at_sender=True)
    await asyncio.sleep(30)
    try:
        for msg_id in setu_msg_id:
            await bot.delete_msg(message_id=msg_id)
    except Exception as e:
        await wp.finish(
            "tx风控了..." + MessageSegment.image(file=erro, cache=False), at_sender=True
        )'''

@re.handle()
async def _(event: MessageEvent):
    user_id = event.user_id
    if not limiter_default.check(user_id):
        left_time = limiter_default.left_time(user_id)
        await re.finish(f"我知道你很非.但是你先别急,cd还有{left_time}秒")
        return

    limiter_default.start_cd(user_id)
    url = await get_redirect_url(
        "https://iw233.cn/api.php?sort=top"
    )  # 确保 get_redirect_url 是 async
    base64_data = await get_msgurl(url)
    try:
        await re.send(
            "看看你的运气{}".format(url) + MessageSegment.image(file=base64_data, cache=False),
            at_sender=True,
        )
    except Exception as e:
        await re.finish("tx风控了..." + str(e))
    else:
        await re.finish()

@food.handle()
async def _(matcher: Matcher, event: MessageEvent):
    user_id = event.user_id
    if not limiter_default.check(user_id):
        left_time = limiter_default.left_time(user_id)
        await matcher.finish(f"我知道你很饿.但是你先别急,cd还有{left_time}秒")
        return

    limiter_default.start_cd(user_id)

    url = await get_redirect_url("https://source.unsplash.com/1600x900/?food")
    await food.finish(MessageSegment.image(file=url, cache=False), at_sender=True)

@daily.handle()
async def _():
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = f"data/daily/{today}.txt"
    if os.path.exists(filepath):
        with open(filepath, "r") as f:
            msg = f.read()
            await daily.finish(
                MessageSegment.image(file=msg, cache=True), at_sender=True
            )
    else:
        await daily.finish("今日新闻未获取到", at_sender=True)

@msn.handle()
async def _():
    url = await get_redirect_url("https://api.vvhan.com/api/bing?rand=sj&size=1920x1680")
    await msn.finish(MessageSegment.image(file=url, cache=False), at_sender=True)

@sese.handle()
async def _(matcher: Matcher, event: MessageEvent):
    url = await get_redirect_url("https://api.vvhan.com/api/girl")

    user_id = event.user_id

    if not limiter_default.check(user_id):
        left_time = limiter_default.left_time(user_id)
        await matcher.finish(f"我知道你想要图.但是你先别急,cd还有{left_time}秒")
        return

    limiter_default.start_cd(user_id)

    await sese.finish(MessageSegment.image(file=url, cache=False), at_sender=True)

@m2.handle()
async def _(matcher: Matcher, event: MessageEvent, bot: Bot):
    user_id = event.user_id
    if not limiter_loong.check(user_id):
        left_time = limiter_loong.left_time(user_id)
        await matcher.finish(f"我知道你急了.但是你先别急,0.5月一次")
    setu_msg_id = []
    limiter_loong.start_cd(user_id)
    url = await get_redirect_url("https://moe.jitsu.top/r18")
    msg_id = (await m2.send("看看你的运气{}".format(url)))["message_id"]
    setu_msg_id.append(msg_id)
    await asyncio.sleep(30)
    try:
        for msg_id in setu_msg_id:
            await bot.delete_msg(message_id=msg_id)
    except Exception as e:
        await matcher.finish("tx风控了..." + str(e))
