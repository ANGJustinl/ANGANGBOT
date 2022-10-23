from nonebot import on_command, on_notice
from nonebot.typing import T_State
from nonebot.adapters.onebot.v11 import Message, Event, Bot, MessageSegment
from nonebot.exception import IgnoredException
from nonebot.message import event_preprocessor
from src.libraries.image import *


@event_preprocessor
async def preprocessor(bot, event, state):
    if hasattr(event, 'message_type') and event.message_type == "private" and event.sub_type != "friend":
        raise IgnoredException("not reply group temp message")

        
help = on_command('help')


@help.handle()
async def _(bot: Bot, event: Event, state: T_State):
    help_str = '''可用命令如下：

setu插件========
命令头: setu|色图|涩图|想色色|来份色色|来份色图|想涩涩|多来点|来点色图|来张setu|来张色图|来点色色|色色|涩涩  (任意一个)
张数: 1 2 3 4 ... 张|个|份  (可不填, 默认1)
r18: 不填则不会出现r18图片, 填了会根据r18模式管理中的数据判断是否可返回r18图片
关键词: 任意 (可不填)
参考 (空格可去掉):   
setu 10张 白丝

基于文心大模型的AI机器人画画插件=========
触发菜单命令：画画帮助 当前支持 古风 油画 水彩画 卡通画 二次元 浮世绘 蒸汽波艺术 low poly 像素风格 概念艺术 未来主义 赛博朋克 写实风格 洛丽塔风格 巴洛克风格 超现实主义 主要擅长风景写意画，请尽量给定比较明确的意象
如：油画 江上落日与晚霞
「公式」= 图片主体，细节词，修饰词

使用wttr.in的天气查询========
"天气 城市名"(可选，如不给出机器人会提示获取)
"天气 城市名_format=v2"
"天气 城市名_format=v3"
指定语言:
"天气 城市名_lang=语言" 语言可选于：
am ar af be bn ca da de el et fr fa hi hu ia id it lt mg nb nl oc pl pt-br ro ru ta tr th uk vi zh-cn zh-tw
甚至支持看月相：
"天气 Moon"

今日运势！=========
一般抽签：今日运势、抽签、运势；
指定主题抽签：[xx抽签]，例如：pcr抽签、holo抽签、碧蓝抽签；
[群管或群主或超管] 配置抽签主题：设置[原神/pcr/东方/vtb/xxx]签：设置群抽签主题；
重置（抽签）主题：设置群抽签主题为随机；
抽签设置：查看当前群抽签主题的配置；
[超管] 刷新抽签：全局即刻刷新抽签，防止过0点未刷新；
今日运势帮助：显示插件帮助文案；
查看（抽签）主题：显示当前已启用主题；

APEX接口========
**查询地图轮换**：【a地图】
**查询制造轮换**：【a制造】
**查询猎杀信息**：【a猎杀】
**绑定烂橘子ID**：【a绑定 烂橘子ID】
**查询玩家信息**：【a查询】(这个需先绑定烂橘子ID)、【a查询 烂橘子ID】

乌蒙DX功能========
今日舞萌 查看今天的舞萌运势
XXXmaimaiXXX什么 随机一首歌
随个[dx/标准][绿黄红紫白]<难度> 随机一首指定条件的乐曲
查歌<乐曲标题的一部分> 查询符合条件的乐曲
[绿黄红紫白]id<歌曲编号> 查询乐曲信息或谱面信息
<歌曲别名>是什么歌 查询乐曲别名对应的乐曲
定数查歌 <定数>  查询定数对应的乐曲
定数查歌 <定数下限> <定数上限>
分数线 <难度+歌曲id> <分数线> 详情请输入“分数线 帮助”查看

ANGAANGBOT POWERED BY NONEBOT2 
反馈与联系
群:696748432
邮箱: angjustin@163.com
github:https://github.com/ANGJustinl/ANGANGBOT/blob/main/README.md'''

    await help.send(Message([
        MessageSegment("image", {
            "file": f"base64://{str(image_to_base64(text_to_image(help_str)), encoding='utf-8')}"
        })
    ]))


async def _group_poke(bot: Bot, event: Event) -> bool:
    value = (event.notice_type == "notify" and event.sub_type == "poke" and event.target_id == int(bot.self_id))
    return value


poke = on_notice(rule=_group_poke, priority=10, block=True)


@poke.handle()
async def _(bot: Bot, event: Event, state: T_State):
    if event.__getattribute__('group_id') is None:
        event.__delattr__('group_id')
    await poke.send(Message([
        MessageSegment("poke",  {
           "qq": f"{event.sender_id}"
       })
    ]))

