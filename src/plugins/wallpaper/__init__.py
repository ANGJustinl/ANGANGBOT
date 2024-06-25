from nonebot import on_command, on_regex
from nonebot.matcher import Matcher
from nonebot.typing import T_State
from nonebot.params import Arg
from nonebot.adapters.onebot.v11 import Message, MessageSegment, Bot, MessageEvent

from .exchange import get_redirect_url
from .limiter import limiter, cd_lim
from .get import get_msgurl
from .post import get_msg
from re import I
import asyncio
from io import BytesIO

###################
from nonebot.plugin import PluginMetadata

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
###################
erro = "https://moetu.org/image/Ur3aj"

food = on_command("美食", aliases={"food"}, priority=5, block=True)
wp = on_command("壁纸", aliases={"wp"}, priority=5, block=True)
re = on_command(
    "运气检测", aliases={"luck", "随机壁纸", "wpwp"}, priority=5, block=True
)
fd = on_command("别在这里发癫", aliases={"fd"}, priority=5, block=True)
regex = r"^(fuck|操|操死|社保|想涩|超死|超市|炒死|焯死)\s?(.*)?"
kkp = on_regex(regex, flags=I, priority=20, block=True)
day_ = on_command("每日新闻", aliases={"news"}, priority=5, block=True)
msn = on_command("msn", priority=5, block=True)
sese = on_command("sese")
mature = on_command("mature", aliases={"r18roll1"}, priority=5, block=True)
m2 = on_command("mature2", aliases={"r18roll2"}, priority=5, block=True)
search = on_command("搜图", aliases={"sc"}, priority=5, block=True)
hle = on_command("impart")


@wp.handle()
async def _handle(matcher: Matcher, event: MessageEvent, bot: Bot):
    user_id = event.user_id
    if not limiter.check(user_id):
        left_time = limiter.left_time(user_id)
        await matcher.finish(f"我知道你急了.但是你先别急,cd还有{left_time}秒")
        return

    limiter.start_cd(user_id)
    url2 = "https://moe.anosu.top/img"
    url = get_redirect_url(url2)
    # url=get_redirect_url("https://iw233.cn/api.php?sort=top")
    try:
        await wp.send(
            "您点的图来了{}".format(url) + MessageSegment.image(file=url, cache=False),
            at_sender=True,
        )
    except Exception as e:
        await wp.finish(
            "tx风控了..." + MessageSegment.image(file=erro, cache=False), at_sender=True
        )
    pass


@mature.handle()
async def _handle(matcher: Matcher, event: MessageEvent, bot: Bot):
    user_id = event.user_id
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
        )


@re.handle()
async def _handle(matcher: Matcher, event: MessageEvent, bot: Bot):
    user_id = event.user_id
    if not limiter.check(user_id):
        left_time = limiter.left_time(user_id)
        await re.finish(f"我知道你很非.但是你先别急,cd还有{left_time}秒")
        return

    limiter.start_cd(user_id)
    msgs = []
    # url =
    url = get_redirect_url("https://iw233.cn/api.php?sort=top")
    base64 = await get_msgurl(url)

    byte_data = BytesIO(base64)
    pic = byte_data.getvalue()

    # url = get_msg2('https://api.lolicon.app/setu/v2')
    try:
        await re.send(
            "看看你的运气{}".format(url) + MessageSegment.image(file=pic, cache=False),
            at_sender=True,
        )
    except Exception as e:
        await re.finish("tx风控了..." + str(e))
    pass


@food.handle()
async def _handle(matcher: Matcher, event: MessageEvent):
    user_id = event.user_id
    if not limiter.check(user_id):
        left_time = limiter.left_time(user_id)
        await matcher.finish(f"我知道你很饿.但是你先别急,cd还有{left_time}秒")
        return

    limiter.start_cd(user_id)

    url = get_redirect_url("https://source.unsplash.com/1600x900/?food")
    # await re.send("haha我不给")
    await food.finish(MessageSegment.image(file=url, cache=False), at_sender=True)


@kkp.handle()
async def _handle(matcher: Matcher, event: MessageEvent):
    url = "https://gchat.qpic.cn/gchatpic_new/7713%209032/1003802944-2292404790-E19D492DCE5C76E6E50E81468340CFDF/0?term=2&amp;is_origin=0]%22"
    await kkp.finish(MessageSegment.image(file=url, cache=True), at_sender=True)


@msn.handle()
async def _handle(matcher: Matcher, event: MessageEvent):
    url = get_redirect_url("https://api.vvhan.com/api/bing?rand=sj&size=1920x1680")
    await msn.finish(MessageSegment.image(file=url, cache=False), at_sender=True)


@day_.handle()
async def _handle(matcher: Matcher, event: MessageEvent):
    url = "https://v2.alapi.cn/api/zaobao"
    token = "VNk9bbtpNdCSO702"
    msg = await get_msg(url, token)
    await day_.finish(MessageSegment.image(file=msg, cache=False), at_sender=True)


@sese.handle()
async def _handle(matcher: Matcher, event: MessageEvent):
    url = get_redirect_url("https://api.vvhan.com/api/girl")

    user_id = event.user_id

    if not limiter.check(user_id):
        left_time = limiter.left_time(user_id)
        await matcher.finish(f"我知道你想要打∠.但是你先别急,cd还有{left_time}秒")
        return

    limiter.start_cd(user_id)

    await sese.finish(MessageSegment.image(file=url, cache=False), at_sender=True)


@m2.handle()
async def _handle(matcher: Matcher, event: MessageEvent, bot: Bot):
    user_id = event.user_id
    if not cd_lim.check(user_id):
        left_time = cd_lim.left_time(user_id)
        await matcher.finish(f"我知道你急了.但是你先别急,0.5月一次")
        return
    setu_msg_id = []
    cd_lim.start_cd(user_id)
    url = get_redirect_url("https://moe.jitsu.top/r18")
    msg_id = (await m2.send("看看你的运气{}".format(url)))["message_id"]
    setu_msg_id.append(msg_id)
    await asyncio.sleep(30)
    try:
        for msg_id in setu_msg_id:
            await bot.delete_msg(message_id=msg_id)
    except:
        pass


@search.got("aim", prompt="请发送搜索目标")
async def get_aim(state: T_State, aim: Message = Arg()):
    urls = aim
    if not str:
        await search.finish("请重新启动并发送目标")

    state["urls"] = urls


@search.handle()
async def _handle(state: T_State, matcher: Matcher, event: MessageEvent):
    aim = state["urls"][0]
    try:
        url = get_redirect_url("https://source.unsplash.com/1600x900/?{}".format(aim))
    except:
        await search.finish("请输入英文")
    # await re.send("haha我不给")
    await search.finish(
        "这是您要的{}".format(aim) + MessageSegment.image(file=url, cache=False),
        at_sender=True,
    )


@hle.handle()
async def _handle(matcher: Matcher, event: MessageEvent):
    url = "https://gchat.qpic.cn/gchatpic_new/77139032/696748432-%202361915796-CD03D3125366BBCD03AEE7FB07E65173/0?term=2&amp;is_origin=0"
    await hle.finish(MessageSegment.image(file=url, cache=True), at_sender=True)


"""   
@arc.handle()
async def _handle(matcher: Matcher,event: MessageEvent,bot:Bot,ms:Message=CommandArg()):    

    num = str(Numbers(ms))
    name = ms.strip([num])
    url=get_redirect_url('https://chart.arisa.moe/'+name+'/'+num+'.webp')
    await arc.send(url)
    try: 
        await arc.send('数字1234为铺面等级'+MessageSegment.image(file=url, cache=False), at_sender=True)
    except Exception as e:
        await arc.finish('lost')"""
