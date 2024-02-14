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
     
# 旧版文档请见 https://github.com/ANGJustinl/ANGANGBOT/README.md (v2以前)


## | 🚀部署 (可参照 https://angjustinl.github.io/2023/01/06/ANGANGBOT1/ )

---

    | 自建可能会遇到各种花里胡哨的麻烦，如果没有一些基础的话，前面可是困难重重啊少年
    
    | 本文内容请您自行判断是否可信可靠可用，若您根据本文内容建立和使用AABT时出了任何问题和不良结果，鄙人概不负责。
    
---

至少需要Python3.8及以上版本(推荐3.10)，可通过python -V或python3 -V查看版本号

此 README 提供了最低程度的基于 nonebot 进行安装的教程与支持。

建议您至少拥有一定的编程基础之后再尝试使用本工具。

1. 安装 Python (推荐>=3.9)
2. 前往 https://github.com/ANGJustinl/ANGANGBOT/releases 下载
3. 安装依赖

推荐使用nb-cil脚手架 `pip install nb-cli` + 在项目的根目录（即 bot.py 文件所在的位置)按下 <kbd>Shift</kbd> + <kbd>右键</kbd>，点击【在此处打开 CMD/PowerShell 窗口】 后

```pip install -r requirements.txt```

3.1 修改 .env.prod 配置文件
```HOST=127.0.0.1 # Nonebot监听的IP-----1
    
PORT=10219 # Nonebot监听的端口-----2
    
LOG_LEVEL=INFO # 日志等级-----3
    
SUPERUSERS=["12345678"] # 超级用户,修改12345678为你bot管理者的qq号-----4
    
NICKNAME=["aabt"] # 机器人的昵称-----5
    
COMMAND_START=[""] # 命令前缀,根据需要自行修改-----6
    
COMMAND_SEP=[" "] # 命令分隔符-----7
```
3.2 修改[.env]配置文件

[pixiv功能](https://github.com/bot-ssttkkl/nonebot-plugin-pixivbot#%E9%85%8D%E7%BD%AE%E9%A1%B9%E4%B8%80%E8%A7%88)

5 ```pixiv_refresh_token = ''``` 写入你p站的refresh_token,具体获取方法自行百度


[setu功能 配置](https://github.com/Special-Week/nonebot_plugin_setu4#env-%E9%85%8D%E7%BD%AE%E9%A1%B9)<- 点我
    
[运势插件](https://github.com/MinatoAquaCrews/nonebot_plugin_fortune#%E5%91%BD%E4%BB%A4)<- 点我

       
|可选填写部分    
|详见[.env]配置文件内容
    
1. 启动bot

使用nb-cil脚手架

Ⅰ.您可以直接在项目的根目录  打开 PowerShell 窗口 输入 `nb run`


运行项目。如果输出如下所示的内容，代表运行成功：(由于第一次安装不加载配置文件,或许会略有不同,不报错就是没问题的)

>    10-20 16:40:30 [SUCCESS] nonebot | NoneBot is initializing...
>    
>    10-20 16:40:31 [SUCCESS] nonebot | Succeeded to import "example1"(这里是被加载的插件)
>    
>    10-20 16:40:32 [SUCCESS] nonebot | Running NoneBot...
>    
>    10-20 16:40:32 [INFO] uvicorn | Started server process [uid]
>    
>    10-20 16:40:32 [INFO] uvicorn | Waiting for application startup.
>    
>    10-20 16:40:32 [INFO] uvicorn | Application startup complete.
>    
>    10-20 16:40:32 [INFO] uvicorn | Uvicorn running on http://ip:port (Press CTRL+C to quit)
    
    
1. 连接 CQ-HTTP   [可自行搜索现版本使用方法 如https://www.bilibili.com/read/cv25444623/]

前往 https://github.com/Mrs4s/go-cqhttp > Releases，下载适合自己操作系统的可执行文件。 go-cqhttp 在初次启动时会询问代理方式，选择反向 websocket 代理即可。之后用任何文本编辑器打开config.yml文件，设置反向 ws 地址、上报方式：

```
servers:
    - ws-reverse:
        universal: ws://ip:port/onebot/v11/ws
```
   
然后设置您的 QQ 号和密码。您也可以不设置密码，选择扫码登陆的方式。

登陆成功后，后台应该会发送一条类似的信息：

> 10-20 16:40:32 [INFO] nonebot | WebSocket Connection from CQHTTP Bot Accepted!
    
至此，您可以和对应的 QQ 号聊天并使用 angangbot 的基础功能了。


## | 插件：

对应插件的功能可以自己查询对应插件有关安装方法,此处先不予整合


## | 引用:
[Nonebot2](https://github.com/nonebot/nonebot2)

## 命令

### 1.[Pic_menu](https://github.com/hamo-reid/nonebot_plugin_PicMenu#%E5%A6%82%E4%BD%95%E4%BD%BF%E7%94%A8%E6%8F%92%E4%BB%B6) <-点我查看

### 2.[AnimalVoice_Convert](https://github.com/ANGJustinl/nonebot_plugin_animalVoice)
 
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
`兽音加密`/`convert` | 否 | 群聊/私聊 | 发送需要加密的文字 |
`兽音解密`/`deconvert` | 否 | 群聊/私聊 | 发送需要解密的文字 |
`切噜一下`/`cherulize` | 否 | 群聊/私聊 | 发送需要解密的文字 |
`切噜～`/`decherulize` | 否 | 群聊/私聊 | 发送需要解密的文字 |

### 3.[wallpaper] 
发送`壁纸`获取一张壁纸

发送 `运气检测`
  
打开随机出一张壁纸

非酋还会刷出来风景图
  
api来自 http://api.iw233.cn/API/index.php

`food` 获取食物


### 4.[nonebot_plugin_setu4](https://github.com/Special-Week/nonebot_plugin_setu4#%E8%8E%B7%E5%8F%96setu) <-点我 查看详解

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

### 5.[nonebot_plugin_weather_lite]()
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

### 6.[nonebot_plugin_fortune](https://github.com/MinatoAquaCrews/nonebot_plugin_fortune#%E5%91%BD%E4%BB%A4)
    
占卜一下你的今日运势！🎉
    
一般抽签：``今日运势、抽签、运势``；

指定主题抽签：`[xx抽签]`，例如：pcr抽签、holo抽签、碧蓝抽签；

[群管或群主或超管] 配置抽签主题：```设置[原神/pcr/东方/vtb/xxx]签```：设置群抽签主题；

``重置（抽签）主题``：设置群抽签主题为随机；

``抽签设置``：查看当前群抽签主题的配置；

[超管] `` 刷新抽签 `` ：全局即刻刷新抽签，防止过0点未刷新；

`` 今日运势帮助 `` ：显示插件帮助文案；

`` 查看（抽签）主题 `` ：显示当前已启用主题；


### 7.[pixiv_bot](https://github.com/bot-ssttkkl/nonebot-plugin-pixivbot#%E8%A7%A6%E5%8F%91%E8%AF%AD%E5%8F%A5)
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

更详细请见 https://github.com/bot-ssttkkl/nonebot-plugin-pixivbot#%E8%A7%A6%E5%8F%91%E8%AF%AD%E5%8F%A5

## | 👥反馈与交流

### Issue for sure

QQ:77139032

群聊:696748432

### <a target="_blank" href="https://qm.qq.com/cgi-bin/qm/qr?k=v4YpojQK_Ginr8S3Ies_jwwKrU-ZzA_m&jump_from=webapi&authKey=wZ/DxqcHHPGuTfBSAhpqzOo3/oiX0iojBCLq9qFymK+daTfwfmZNAoQrKIH+o8N0">点我加入群聊</a>

bilibili:https://space.bilibili.com/213993950

tg:https://t.me/angangbot

---
## | 更新记录
v2.5.4 2024.02.14 新版文档与全平台适配

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
- [x] 重写机器人
- [x] 重写文档
- [ ] Steam_asf的bot进行qq控制 <img src="https://progress-bar.dev/20/" alt="bar">

# | EXTRA:
https://afdian.net/a/angjustinl
