# ANGANGBOT
基于小派萌和NoneBot2修改


## | 插件：
nonebot-plugin-status：https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status

NoneBot Plugin R6s：https://github.com/abrahum/nonebot_plugin_r6s

nonebot-plugin-autohelp：https://github.com/ffreemt/nonebot-plugin-autohelp

nonebot_plugin_setu4:https://github.com/Special-Week/nonebot_plugin_setu4

nonebot-bison:https://github.com/felinae98/nonebot-bison

nonebot-plugin-drawer:https://github.com/CrazyBoyM/nonebot-plugin-drawer

nonebot_plugin_weather_lite:https://github.com/zjkwdy/nonebot_plugin_weather_lite

60s读世界:https://github.com/bingganhe123/60s-

## | 引用:
Nonebot2                  https://github.com/nonebot/nonebot2

小派蒙|LittlePaimon       https://github.com/nonebot/nonebot2


# 命令
[nonebot-plugin-status]
    ✨ NoneBot 服务器状态（CPU, Memory, Disk Usage）查看插件✨:
        向机器人发送戳一戳表情
        双击机器人头像戳一戳

[noneBot_plugin_R6s]
    Rainbow Six Siege Players Searcher For Nonebot2:
    
        指令	         别名	         可接受参数	         功能

        r6s	               彩虹六号，r6	         昵称	         查询玩家基本信息

        r6spro	         r6pro，R6pro	         昵称	         查询玩家进阶信息

        r6sops	         r6ops，R6ops	         昵称	         查询玩家干员信息

        r6sp	         r6p，R6p	         昵称	         查询玩家 近期对战 历史段位信息

        r6sset	         r6set，R6set	         昵称	         设置玩家昵称，设置后其余指令可以不带昵称即查询已设置昵称信息

[nonebot_plugin_setu4]
    内置数据库的setu插件:

        命令头: setu|色图|涩图|想色色|来份色色|来份色图|想涩涩|多来点|来点色图|来张setu|来张色图|来点色色|色色|涩涩  (任意一个)

        张数: 1 2 3 4 ... 张|个|份  (可不填, 默认1)

        r18: 不填则不会出现r18图片, 填了会根据r18模式管理中的数据判断是否可返回r18图片

        关键词: 任意 (可不填)

        参考 (空格可去掉):   

            setu 10张 r18 白丝

            setu 10张 白丝
    
            setu r18 白丝
    
            setu 白丝
    
            setu

[nonebot-plugin-drawer]
    基于文心大模型的AI机器人画画插件:
        
        触发菜单命令：画画帮助 当前支持 古风 油画 水彩画 卡通画 二次元 浮世绘 蒸汽波艺术 low poly 像素风格 概念艺术 未来主义 赛博朋克 写实风格 洛丽塔风格 巴洛克风格 超现实主义 主要擅长风景写意画，请尽量给定比较明确的意象

        如：油画 江上落日与晚霞

        api申请https://wenxin.baidu.com/younger/apiDetail?id=20008

[nonebot_plugin_weather_lite]
    使用wttr.in的天气查询:
        命令：

            {注：1.以下天气命令均可以使用wttr、weather、tianqi等效替代,

                2.城市名可以使用各种语言，例如Beijing、Peking、北京是等效的。

                3.支持查询全球各种地区。例如莫斯科什么的都可以。}

            "天气 城市名"(可选，如不给出机器人会提示获取)

            "天气 城市名_format=v2"

            "天气 城市名_format=v3"

            指定语言:
                "天气 城市名_lang=语言" 语言可选于：

                am ar af be bn ca da de el et fr fa hi hu ia id it lt mg nb nl oc pl pt-br ro ru ta tr th uk vi zh-cn zh-tw

            甚至支持看月相：

                "天气 Moon"

            更多用法请参考wttr.in的文档！
                地址：https://github.com/chubin/wttr.in

[60s读世界]
    定时向指定群或列表好友发送每日60s读世界
        注：python3.9以上版本才能正常使用

        在nonebot的env配置文件中输入以下内容

        {#定时发送配置
        read_qq_friends=[12345678910] #设定要发送的QQ好友
        read_qq_groups=[123456789,123456789,123456789] #设定要发送的群
        read_inform_time=[{"HOUR":9,"MINUTE":1}] #在输入时间的时候 不要 以0开头如{"HOUR":06,"MINUTE":08}是错误的}
        ~~不要复制tab~~


# 反馈

Issue for sure

QQ:77139032

mail:angjustin@163.com

bilibili:ANGJustinl










## | 目标:
- [ ] Steam_asf的bot进行qq控制 <img src="https://progress-bar.dev/0/" alt="bar">
