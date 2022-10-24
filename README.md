<p align="center">
  <a href="https://github.com/ANGJustinl/ANGANGBOT"><img src="https://github.com/ANGJustinl/ANGANGBOT/blob/main/repository-open-graph-template.png" width="800" height="400" alt="aabt"></a>
</p>



<div align="center">

# ANGANGBOT

✨ 基于NoneBot2的交互bot ✨
</div>

<p align="center">
  <a>
  <img src="https://img.shields.io/badge/python-3.10-blue.svg" alt="python">
  <img src="https://img.shields.io/badge/Onebot-v11-lightgrey" alt="onebot11">
  <img src="https://img.shields.io/badge/nonebot-2.0.0b4-orange" alt="nonebot2">
  [![Github last commit date](https://img.shields.io/github/last-commit/ANGJustinl/ANGANGBOT.svg?label=Updated&logo=github&cacheSeconds=600)]
  </a>
</p>

    一切开发旨在学习，请勿用于非法用途
    
## | 🚀部署

---

    | 自建可能会遇到各种花里胡哨的麻烦，如果没有一些基础的话，前面可是困难重重啊少年
    
    | 本文内容请您自行判断是否可信可靠可用，若您根据本文内容建立和使用AABT时出了任何问题和不良结果，鄙人概不负责。
    
---

至少需要Python3.9及以上版本(推荐3.10)，可通过python -V或python3 -V查看版本号

此 README 提供了最低程度的基于 nonebot 进行安装的教程与支持。

建议您至少拥有一定的编程基础之后再尝试使用本工具。

1. 安装 Python

2. 安装依赖

推荐使用powershell + nb-cil脚手架

    Ⅰ.在项目的根目录（即 bot.py 文件所在的位置)按下 Shift + 右键，点击【在此处打开 PowerShell 窗口】
    
    Ⅱ. pip install -r requirements.txt

3.1 修改[.env.prod]配置文件
    
    HOST=127.0.0.1 # Nonebot监听的IP-----1
    
    PORT=10219 # Nonebot监听的端口-----2
    
    LOG_LEVEL=INFO # 日志等级-----3
    
    SUPERUSERS=["12345678"] # 超级用户,修改12345678为你bot管理者的qq号-----4
    
    NICKNAME=["aabt"] # 机器人的昵称-----5
    
    COMMAND_START=[""] # 命令前缀,根据需要自行修改-----6
    
    COMMAND_SEP=[" "] # 命令分隔符-----7

3.2 修改[.env]配置文件 22-25行

    #WENXIN
    
    
    wenxin_ak = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"这行填入文心模型的api
    
    wenxin_sk = "XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX"这行填入文心模型的密钥
    


4. 启动bot

        > 舞萌dx插件需额外下载src文件夹进行替换
        
        > 资源文件仅供学习交流使用，请自觉在下载 24 小时内删除资源文件。

        > 在运行代码之前，您需要从此链接https://www.diving-fish.com/maibot/static.zip

        > 下载资源文件并解压到src文件夹中

推荐使用powershell + nb-cil脚手架

    Ⅰ.您可以直接在项目的根目录（即 bot.py 文件所在的位置)按下 Shift + 右键，点击【在此处打开 PowerShell 窗口】

    Ⅱ.nb run

运行项目。如果输出如下所示的内容，代表运行成功：>(由于第一次安装不加载配置文件,或许会略有不同,不报错就是没问题的)

    10-20 16:40:30 [SUCCESS] nonebot | NoneBot is initializing...
    10-20 16:40:30 [INFO] nonebot | Current Env: prod
    [I 221020 16:40:31 nonebot_plugin_autohelp:45] Loaded plugins: ['nonebot_plugin_autohelp']
    10-20 16:40:31 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_autohelp"
    10-20 16:40:31 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_weather_lite"
    10-20 16:40:31 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_setu4"
    10-20 16:40:32 [SUCCESS] nonebot | Succeeded to import "maimaidx"
    10-20 16:40:32 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_status"
    10-20 16:40:32 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_couplets"
    10-20 16:40:32 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_r6s"
    10-20 16:40:32 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_drawer"
    10-20 16:40:32 [SUCCESS] nonebot | Succeeded to import "public"
    10-20 16:40:32 [SUCCESS] nonebot | Succeeded to import "auto_agree"
    10-20 16:40:32 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_hammer_nbnhhsh"

    10-20 16:40:32 [SUCCESS] nonebot | Running NoneBot...
    10-20 16:40:32 [INFO] uvicorn | Started server process [16676]
    10-20 16:40:32 [INFO] uvicorn | Waiting for application startup.
    10-20 16:40:32 [INFO] uvicorn | Application startup complete.
    10-20 16:40:32 [INFO] uvicorn | Uvicorn running on http://127.0.0.1:10219 (Press CTRL+C to quit)
    
    
5. 连接 CQ-HTTP

前往 https://github.com/Mrs4s/go-cqhttp > Releases，下载适合自己操作系统的可执行文件。 go-cqhttp 在初次启动时会询问代理方式，选择反向 websocket 代理即可。
之后用任何文本编辑器打开config.yml文件，设置反向 ws 地址、上报方式：

    message:
      post-format: array

    servers:
      - ws-reverse:
          universal: ws://127.0.0.1:10219/onebot/v11/ws
          
然后设置您的 QQ 号和密码。您也可以不设置密码，选择扫码登陆的方式。

登陆成功后，后台应该会发送一条类似的信息：

    10-20 16:40:32 [INFO] nonebot | WebSocket Connection from CQHTTP Bot 114514 Accepted!
    
至此，您可以和对应的 QQ 号聊天并使用 angangbot 的基础功能了。


## | 插件：

对应插件的功能可以自己查询对应插件有关安装方法,此处先不予整合



## | 插件：
nonebot-plugin-status：https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status

NoneBot Plugin R6s：https://github.com/abrahum/nonebot_plugin_r6s

nonebot-plugin-autohelp：https://github.com/ffreemt/nonebot-plugin-autohelp

nonebot_plugin_setu4:https://github.com/Special-Week/nonebot_plugin_setu4

nonebot-bison:https://github.com/felinae98/nonebot-bison

nonebot-plugin-drawer:https://github.com/CrazyBoyM/nonebot-plugin-drawer

nonebot_plugin_weather_lite:https://github.com/zjkwdy/nonebot_plugin_weather_lite

Nonebot Plugin Hammer Nbnhhsh:https://github.com/ArgonarioD/nonebot-plugin-hammer-nbnhhsh

nonebot-plugin-treehelp:https://github.com/he0119/nonebot-plugin-treehelp

nonebot_plugin_fortune:https://github.com/MinatoAquaCrews/nonebot_plugin_fortune

Apex_Tool APEX英雄QQBot信息查询:https://github.com/AreCie/Apex_Tool

[HarukaBot]https://github.com/SK-415/HarukaBot

## | 引用:
Nonebot2                  https://github.com/nonebot/nonebot2

小派蒙|LittlePaimon       https://github.com/nonebot/nonebot2

mai bot                   https://github.com/Diving-Fish/mai-bot

HarukaBot                 https://github.com/SK-415/HarukaBot


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
        
        「公式」= 图片主体，细节词，修饰词

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

[nonebot_plugin_fortune]
    
    占卜一下你的今日运势！🎉
    
        一般抽签：今日运势、抽签、运势；

        指定主题抽签：[xx抽签]，例如：pcr抽签、holo抽签、碧蓝抽签；

        [群管或群主或超管] 配置抽签主题：设置[原神/pcr/东方/vtb/xxx]签：设置群抽签主题；

        重置（抽签）主题：设置群抽签主题为随机；

        抽签设置：查看当前群抽签主题的配置；

        [超管] 刷新抽签：全局即刻刷新抽签，防止过0点未刷新；

        今日运势帮助：显示插件帮助文案；

        查看（抽签）主题：显示当前已启用主题；


[HarukaBot b站推送]

（请将UID替换为需要操作的B站UID）

关闭全体 UID

开启全体 UID

开启动态 UID

关闭动态 UID

关闭直播 UID

开启直播 UID

关闭权限

开启权限

关注 UID

取关 UID

关注列表

未改配置群聊中请@机器人使用

---
[APEX接口功能]
   **查询地图轮换**：【a地图】

   **查询制造轮换**：【a制造】
 
   **查询猎杀信息**：【a猎杀】
 
   **绑定烂橘子ID**：【a绑定 烂橘子ID】
 
   **查询玩家信息**：【a查询】(这个需先绑定烂橘子ID)、【a查询 烂橘子ID】

>[60s读世界]失效未启用
    定时向指定群或列表好友发送每日60s读世界
        注：python3.9以上版本才能正常使用

        在nonebot的env配置文件中输入以下内容

        {#定时发送配置
        read_qq_friends=[12345678910] #设定要发送的QQ好友
        read_qq_groups=[123456789,123456789,123456789] #设定要发送的群
        read_inform_time=[{"HOUR":9,"MINUTE":1}] #在输入时间的时候 不要 以0开头如{"HOUR":06,"MINUTE":08}是错误的}
        


## | 👥反馈与交流

Issue for sure

QQ:77139032

群聊:696748432

<a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=v4YpojQK_Ginr8S3Ies_jwwKrU-ZzA_m&jump_from=webapi&authKey=wZ/DxqcHHPGuTfBSAhpqzOo3/oiX0iojBCLq9qFymK+daTfwfmZNAoQrKIH+o8N0"><img border="0" src="//pub.idqqimg.com/wpa/images/group.png" alt="ANGANGBOT研磨会" title="ANGANGBOT研磨会"></a>

mail:angjustin@163.com

bilibili:https://space.bilibili.com/213993950?spm_id_from=333.1007.0.0



---
## | 更新记录

v1.1.6 2022.10.23 重写了help获取帮助命令cv2内容

v1.1.5 2022.10.22 配置了APEX查分插件，改了部分插件内容

v1.1.4 2022.10.22 添加舞萌DX插件相关内容

v1.1.2 2022.10.21 添加了部分插件，优化了requirements.txt内容

v1.1.0 2022.10.20 上传至git

v1.0.1 2022.10.19 完成了bot的配置流程

v1.0.0 2022.10.19 bot初步成型

---
## | 目标:
- [ ] Steam_asf的bot进行qq控制 <img src="https://progress-bar.dev/5/" alt="bar">

# | EXTRA:
https://afdian.net/a/angjustinl
