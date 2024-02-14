<p align="center">
  <a href="[https://github.com/ANGJustinl/ANGANGBOT"><img src="https://github.com/ANGJustinl/angjustinl.github.io/blob/main/repository-open-graph-template%20%5B%E5%8E%9F%E5%A7%8B%E5%A4%A7%E5%B0%8F%5D.jpg" width="800" height="400" alt="aabt"></a>
</p>



<div align="center">

# ANGANGBOT

✨ 基于NoneBot2的交互bot ✨
</div>

<p align="center">
<a href="https://www.python.org">
  <img src="https://img.shields.io/github/languages/top/angjustinl/nonebot_plugin_face2cartoonpic_main" alt="languages">
</a>  
<img src="https://img.shields.io/badge/python-3.10-blue.svg" alt="python">
<img src="https://img.shields.io/badge/Onebot-v11-lightgrey" alt="onebot11">
<img src="https://img.shields.io/badge/nonebot-2.0.0b4-orange" alt="nonebot2">
<img src="https://img.shields.io/github/last-commit/ANGJustinl/ANGANGBOT.svg?label=Updated&logo=github&cacheSeconds=600" alt="AABT">   
<img src="https://img.shields.io/github/downloads/ANGJustinl/ANGANGBOT/total.svg?label=Downloads&logo=github&cacheSeconds=600" alt="AABT">   

![Alt](https://repobeats.axiom.co/api/embed/6a22c5e973a99b3a396f90ccde21ecfc25c0c2b8.svg "Repobeats analytics image")

 
</p>

    一切开发旨在学习，请勿用于非法用途
     
# 新版文档请见 https://github.com/ANGJustinl/ANGANGBOT/README.md (v2+)


## | 🚀部署 (可参照 https://angjustinl.github.io/2023/01/06/ANGANGBOT1/ )

---

    | 自建可能会遇到各种花里胡哨的麻烦，如果没有一些基础的话，前面可是困难重重啊少年
    
    | 本文内容请您自行判断是否可信可靠可用，若您根据本文内容建立和使用AABT时出了任何问题和不良结果，鄙人概不负责。
    
---

至少需要Python3.9及以上版本(推荐3.10)，可通过python -V或python3 -V查看版本号

此 README 提供了最低程度的基于 nonebot 进行安装的教程与支持。

建议您至少拥有一定的编程基础之后再尝试使用本工具。

1. 安装 Python

2. 前往 https://github.com/ANGJustinl/ANGANGBOT/releases 下载lite文件并解压至本地

3. 下载需要的资源文件 
	
	>部分插件需额外下载src文件夹进行替换    
	>
	>资源文件仅供学习交流使用，请自觉在下载 24 小时内删除资源文件。
	>
	>在运行代码之前，您需要从此链接 https://cowtransfer.com/s/c7fa24d11b3949 [传输口令 rt318w]
	>
	>下载资源文件并解压到src文件夹中

4. 安装依赖

推荐使用powershell + nb-cil脚手架

Ⅰ. ```pip install nb-cli```

Ⅱ.在项目的根目录（即 bot.py 文件所在的位置)按下 <kbd>Shift</kbd> + <kbd>右键</kbd>，点击【在此处打开 PowerShell 窗口】
    
Ⅲ. ```pip install -r requirements.txt```

3.1 修改[.env.prod]配置文件
```HOST=127.0.0.1 # Nonebot监听的IP-----1
    
PORT=10219 # Nonebot监听的端口-----2
    
LOG_LEVEL=INFO # 日志等级-----3
    
SUPERUSERS=["12345678"] # 超级用户,修改12345678为你bot管理者的qq号-----4
    
NICKNAME=["aabt"] # 机器人的昵称-----5
    
COMMAND_START=[""] # 命令前缀,根据需要自行修改-----6
    
COMMAND_SEP=[" "] # 命令分隔符-----7
```
3.2 修改[.env]配置文件

pixiv功能
5 ```pixiv_refresh_token = ''``` 写入你p站的refresh_token,具体获取方法自行百度

apex功能
27 ``` apex_api_key = "" ``` https://portal.apexlegendsapi.com/ 获取token
    
腾讯云人像变化    
30 `Secret_Id = ""`
31 ```Secret_Key = ""``` 
       
|可选填写部分    
|详见[.env]配置文件内容
    
4. 启动bot

>部分插件需额外下载src文件夹进行替换    
>
>资源文件仅供学习交流使用，请自觉在下载 24 小时内删除资源文件。
>
>在运行代码之前，您需要从此链接 https://cowtransfer.com/s/c7fa24d11b3949 [传输口令 rt318w]
>
>下载资源文件并解压到src文件夹中

推荐使用powershell + nb-cil脚手架

Ⅰ.您可以直接在项目的根目录（即 bot.py 文件所在的位置)按下 Shift + 右键，点击【在此处打开 PowerShell 窗口】
Ⅱ.

nb run


运行项目。如果输出如下所示的内容，代表运行成功：(由于第一次安装不加载配置文件,或许会略有不同,不报错就是没问题的)

>    10-20 16:40:30 [SUCCESS] nonebot | NoneBot is initializing...
>    
>    10-20 16:40:30 [INFO] nonebot | Current Env: prod
>    
>    10-20 16:40:31 [SUCCESS] nonebot | Succeeded to import "nonebot_plugin_weather_lite"
>    
>    ......(这里是被加载的插件)
>    
>    10-20 16:40:32 [SUCCESS] nonebot | Running NoneBot...
>    
>    10-20 16:40:32 [INFO] uvicorn | Started server process [16676]
>    
>    10-20 16:40:32 [INFO] uvicorn | Waiting for application startup.
>    
>    10-20 16:40:32 [INFO] uvicorn | Application startup complete.
>    
>    10-20 16:40:32 [INFO] uvicorn | Uvicorn running on http://127.0.0.1:10219 (Press CTRL+C to quit)
    
    
5. 连接 CQ-HTTP

前往 https://github.com/Mrs4s/go-cqhttp > Releases，下载适合自己操作系统的可执行文件。 go-cqhttp 在初次启动时会询问代理方式，选择反向 websocket 代理即可。之后用任何文本编辑器打开config.yml文件，设置反向 ws 地址、上报方式：

```message:
    post-format: array

servers:
    - ws-reverse:
        universal: ws://127.0.0.1:10219/onebot/v11/ws
```
   
然后设置您的 QQ 号和密码。您也可以不设置密码，选择扫码登陆的方式。

登陆成功后，后台应该会发送一条类似的信息：

> 10-20 16:40:32 [INFO] nonebot | WebSocket Connection from CQHTTP Bot 114514 Accepted!
    
至此，您可以和对应的 QQ 号聊天并使用 angangbot 的基础功能了。


## | 插件：

对应插件的功能可以自己查询对应插件有关安装方法,此处先不予整合



## | 插件：
nonebot-plugin-status：https://github.com/cscs181/QQ-GitHub-Bot/tree/master/src/plugins/nonebot_plugin_status

nonebot_plugin_setu4:https://github.com/Special-Week/nonebot_plugin_setu4

nonebot_plugin_weather_lite:https://github.com/zjkwdy/nonebot_plugin_weather_lite

Nonebot Plugin Hammer Nbnhhsh:https://github.com/ArgonarioD/nonebot-plugin-hammer-nbnhhsh

nonebot_plugin_fortune:https://github.com/MinatoAquaCrews/nonebot_plugin_fortune

...... 目前文档任有不全,具体插件详见指令


## | 引用:
[Nonebot2]                  https://github.com/nonebot/nonebot2

[mai-bot]                   https://github.com/Diving-Fish/mai-bot

[HarukaBot]                 https://github.com/SK-415/HarukaBot


## 命令

[Pic_menu] 
  菜单
      菜单 4 2


[AnimalVoice_Convert] 
`兽音加密`/`convert` | 否 | 群聊/私聊 | 发送需要加密的文字 |
`兽音解密`/`deconvert` | 否 | 群聊/私聊 | 发送需要解密的文字 |
`切噜一下`/`cherulize` | 否 | 群聊/私聊 | 发送需要解密的文字 |
`切噜～`/`decherulize` | 否 | 群聊/私聊 | 发送需要解密的文字 |

[wallpaper] 
发送`壁纸`获取一张壁纸

发送 `运气检测`
  
打开随机出一张壁纸

非酋还会刷出来风景图
  
api来自 http://api.iw233.cn/API/index.php

`food` 获取食物
  
`sc + 搜索目标`搜图

[nonebot-plugin-status]
✨ NoneBot 服务器状态（CPU, Memory, Disk Usage）查看插件✨:
向机器人发送戳一戳表情
`双击机器人头像戳一戳`


[nonebot_plugin_setu4]
内置数据库的setu插件:

命令头: `setu|色图|涩图|想色色|来份色色|来份色图|想涩涩|多来点|来点色图|来张setu|来张色图|来点色色|色色|涩涩`  (任意一个)

张数: `1 2 3 4 ... 张|个|份`  (可不填, 默认1)

`r18`: 不填则不会出现r18图片, 填了会根据r18模式管理中的数据判断是否可返回r18图片

关键词: 任意 (可不填)

参考 (空格可去掉):   

> setu 10张 r18 白丝
> setu 10张 白丝    
> setu r18 白丝    
> setu 白丝
> setu

[nonebot-plugin-drawer] 目前因为文心接口原因停止使用
基于文心大模型的AI机器人画画插件:
        
触发菜单命令：`画画帮助 当前支持 古风 油画 水彩画 卡通画 二次元 浮世绘 蒸汽波艺术 low poly 像素风格 概念艺术 未来主义 赛博朋克 写实风格 洛丽塔风格 巴洛克风格 超现实主义` 主要擅长风景写意画，请尽量给定比较明确的意象

如：```油画 江上落日与晚霞```
        
>「公式」= 图片主体，细节词，修饰词

api申请https://wenxin.baidu.com/younger/apiDetail?id=20008

[nonebot_plugin_weather_lite]
使用wttr.in的天气查询:
命令：

注：
    
    1.以下天气命令均可以使用wttr、weather、tianqi等效替代,

    2.城市名可以使用各种语言，例如Beijing、Peking、北京是等效的。

    3.支持查询全球各种地区。例如莫斯科什么的都可以。

``"天气 城市名"`` (可选，如不给出机器人会提示获取)

`"天气 城市名_format=v2"`

``"天气 城市名_format=v3"``

指定语言:

```
天气 城市名_lang=语言
``` 

语言可选于：

>am ar af be bn ca da de el et fr fa hi hu ia id it lt mg nb nl oc pl pt-br ro ru ta tr th uk vi zh-cn zh-tw

甚至支持看月相：

```
"天气 Moon"
```

更多用法请参考wttr.in的文档！
地址：https://github.com/chubin/wttr.in

[nonebot_plugin_fortune]
    
占卜一下你的今日运势！🎉
    
一般抽签：``今日运势、抽签、运势``；

指定主题抽签：`[xx抽签]`，例如：pcr抽签、holo抽签、碧蓝抽签；

[群管或群主或超管] 配置抽签主题：```设置[原神/pcr/东方/vtb/xxx]签```：设置群抽签主题；

``重置（抽签）主题``：设置群抽签主题为随机；

``抽签设置``：查看当前群抽签主题的配置；

[超管] `` 刷新抽签 `` ：全局即刻刷新抽签，防止过0点未刷新；

`` 今日运势帮助 `` ：显示插件帮助文案；

`` 查看（抽签）主题 `` ：显示当前已启用主题；


[HarukaBot b站推送]

（请将UID替换为需要操作的B站UID）

```
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
```
  
[savor]
```分析 + 图片 分析图片tag```

[pixiv_bot]
`看看<类型>榜<范围>`：查看pixiv榜单 <类型>可省略
  
`来<数量>张图`：从推荐插画随机抽选一张插画（<数量>可省略，下同）
  
`来<数量>张<关键字>图`：搜索关键字，从搜索结果随机抽选一张插画
  
>示例：来张初音ミク图、来五张初音ミク图
      
`来<数量>张<用户>老师的图`：搜索用户，从插画列表中随机抽选一张插画
  
`看看图<插画ID>`：查看ID对应的插画
  
>示例：看看图114514
      
`来<数量>张私家车`：从书签中随机抽选一张插画（发送者需绑定Pixiv账号，或者在配置中指定默认Pixiv账号）

`/pixivbot bind <pixiv_user_id>`：绑定Pixiv账号（用于随机书签功能）
  
`/pixivbot unbind`：解绑Pixiv账号

`/pixivbot`、`/pixivbot help`：查看帮助

[face2cartoonpic]
`人像变换 + 图片` 可以实现qq的变脸功能

[maimaidx]
`今日舞萌` 查看今天的舞萌运势

`XXXmaimaiXXX什么` 随机一首歌

`随个[dx/标准][绿黄红紫白]<难度>` 随机一首指定条件的乐曲

`查歌<乐曲标题的一部分>` 查询符合条件的乐曲

`[绿黄红紫白]id<歌曲编号>` 查询乐曲信息或谱面信息

`<歌曲别名>是什么歌` 查询乐曲别名对应的乐曲

`定数查歌 <定数>`  查询定数对应的乐曲

`定数查歌 <定数下限> <定数上限>`

`分数线 <难度+歌曲id> <分数线>` 详情请输入“分数线 帮助”查看

---


## | 👥反馈与交流

### Issue for sure

QQ:77139032

群聊:696748432

<a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=v4YpojQK_Ginr8S3Ies_jwwKrU-ZzA_m&jump_from=webapi&authKey=wZ/DxqcHHPGuTfBSAhpqzOo3/oiX0iojBCLq9qFymK+daTfwfmZNAoQrKIH+o8N0"><img border="0" src="//pub.idqqimg.com/wpa/images/group.png" alt="ANGANGBOT研磨会" title="ANGANGBOT研磨会"></a>

mail:angjustin@163.com

bilibili:https://space.bilibili.com/213993950?spm_id_from=333.1007.0.0

tg:https://t.me/angangbot

---
## | 更新记录
v2.0.0 2023.09.01 完全重置 适配最新nb

v1.3.2 2023.01.13 细化了github readme

v1.3.1 2023.01.05 编辑了文档

v1.3 2022 12.30 推倒重来了大部分内容,1.3后的详见新的分支

v1.2 2022.12.20 

v1.1.6 2022.10.23 重写了help获取帮助命令cv2内容

v1.1.5 2022.10.22 配置了APEX查分插件，改了部分插件内容

v1.1.4 2022.10.22 添加舞萌DX插件相关内容

v1.1.2 2022.10.21 添加了部分插件，优化了requirements.txt内容

v1.1.0 2022.10.20 上传至git

v1.0.1 2022.10.19 完成了bot的配置流程

v1.0.0 2022.10.19 bot初步成型

---
## | 目标:
- [ ] Steam_asf的bot进行qq控制 <img src="https://progress-bar.dev/20/" alt="bar">

# | EXTRA:
https://afdian.net/a/angjustinl
