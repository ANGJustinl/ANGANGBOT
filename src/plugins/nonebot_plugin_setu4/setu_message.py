setu_sendmessage = [
    "这是你的🐍图",
    "喏，图",
    "给给给个🐍图",
    "色图有我好冲吗？",
    "有什么好色图有给发出来让大伙看看！",
    "没有，有也不给（骗你的～）",
    "这么喜欢色图呢？不如来点昂昂bot色图？",
    "hso！",
    "不许导，积回去！",
    "∫1/(1+x^4)dx",
    "注意身体，色图看太多对身体不好",
]
setu_sendcd = [
    "憋住，不准冲！",
    "你的色图不出来了！",
    "注意身体，色图看太多对身体不好",
    "憋再冲了！",
    "呃...好像冲了好多次...感觉不太好呢...",
    "这么喜欢bot我, 快来关注昂昂bot -> qq群696748432",
    "你急啥呢？",
]

HELP_MSG = r"""setu指令:
^(setu|色图|涩图|想色色|来份色色|来份色图|想涩涩|多来点|来点色图|来张setu|来张色图|来点色色|色色|涩涩)\s?([x|✖️|×|X|*]?\d+[张|个|份]?)?\s?(r18)?\s?(.*)?

白名单管理：
setu_wl add  添加会话至白名单 eg: setu_wl add user_114514/group_1919810
setu_wl del  移出会话自白名单 eg: setu_wl del user_114514/group_1919810

黑名单管理：    
setu_ban add  添加会话至黑名单 eg: setu_ban add user_114514/group_1919810
setu_ban del  移出会话自黑名单 eg: setu_ban del user_114514/group_1919810

r18模式管理:
setu_r18 on  开启会话的r18模式 eg: setu_r18 on group_1919810
setu_r18 off 关闭会话的r18模式 eg: setu_r18 off group_1919810

cd时间更新:
setu_cd xxx  更新会话的冷却时间, xxx为int类型的参数 eg: setu_cd 10 group_1919810

撤回时间更新:
setu_wd xxx  撤回前等待的时间, xxx为int类型的参数 eg: setu_wd 10 group_1919810

最大张数更新:
setu_mn xxx  单次发送的最大图片数, xxx为int类型的参数   eg: setu_mn 10 group_1919810

查询黑白名单:
setu_roster

更换代理:
setu_proxy xxx  xxx为代理url, 例如i.pixiv.re"""
