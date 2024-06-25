# | 插件 ✨
昂昂Bot 是标准的 Nonebot2 机器人

因此可以任意接入任何 支持Nonebot2 Plugin规范的插件

## | 原生插件 🧡：
### 1. [AnimalVoice_Convert](https://github.com/ANGJustinl/nonebot_plugin_animalVoice) | 兽语/切噜切噜 文本加密插件

<details>
#### ✔ 使用例

![3`$HP~HVN%SK(IV@2HO7X{M](https://user-images.githubusercontent.com/96008766/210118707-b00e90ff-ce8c-4fdb-bcd9-f3a18c2ebc50.png)

![OYJ5N2~Z@XZ)B6FL %MEIKA](https://user-images.githubusercontent.com/96008766/210118729-8e8a6ff0-f911-4514-aac9-a87f714051e9.png)

#### 🎉 使用
指令表
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| [兽音加密]/[convert] | 否 | 群聊/私聊 | 发送需要加密的文字 |
| [兽音解密]/[deconvert] | 否 | 群聊/私聊 | 发送需要解密的文字 |
| [切噜一下]/[cherulize] | 否 | 群聊/私聊 | 发送需要解密的文字 |
| [切噜～]/[decherulize] | 否 | 群聊/私聊 | 发送需要解密的文字 |
| [译者帮助] | 否 | 群聊/私聊 | 发送帮助 |

**注意**
默认情况下, 您应该在指令前加上命令前缀, 通常是 /

#### 🛠 配置项

| 配置项 | 类型 | 说明 |
|:-----:|:----:|:----:|
| customize_cmd_animalconvert | str | 自定义触发兽音加密命令 |
| customize_cmd_animaldeconvert | str | 自定义触发兽音解密命令 |
| customize_cmd_cherulizing | str | 自定义触发切噜一下命令 |
| customize_cmd_decherulizing | str | 自定义触发切噜～命令 |
</details>

### 2.[Fortune](https://github.com/ANGJustinl/) | 今日运势占卜
<details>

### 命令

1. 一般抽签：今日运势、抽签、运势；

2. 抽签设置：查看当前群抽签主题的配置；

3. 今日运势帮助：显示插件帮助文案；
### 本插件改自[nonebot_plugin_fortune](https://github.com/MinatoAquaCrews/nonebot_plugin_fortune)

### 抽签图片及文案资源

1. [opqqq-plugin](https://github.com/opq-osc/opqqq-plugin)：PCR；

2. 感谢江樂丝提供东方签底；

3. 东方归言录(Touhou Lostword)：[KafCoppelia](https://github.com/KafCoppelia)；

4. [FloatTech-zbpdata/Fortune](https://github.com/FloatTech/zbpdata)：其余主题签；

5. 战舰少女R(Warship Girls R)：[veadex](https://github.com/veadex)、[EsfahanMakarov](https://github.com/EsfahanMakarov)；

6. 运势文案：[KafCoppelia](https://github.com/KafCoppelia)。`copywriting.json` 整合了関係運、全体運、勉強運、金運、仕事運、恋愛運、総合運、大吉、中吉、小吉、吉、半吉、末吉、末小吉、凶、小凶、半凶、末凶、大凶及700+条运势文案！来源于Hololive早安系列2019年第6.10～9.22期，有修改。

</details>

### 3.[wallpaper](https://github.com/ANGJustinl/ANGANGBOT) | 壁纸插件
<details>

### 命令
发送`壁纸`获取一张壁纸

发送 `运气检测`
  
打开随机出一张壁纸

非酋还会刷出来风景图
  
api来自 http://api.iw233.cn/API/index.php

`food` 获取食物
</details>

### 4.[Httpcat](https://github.com/ANGJustinl/nonebot_plugin_HttpCat) | http猫猫插件
<details>

### 🎉 使用
#### 指令表
| 指令 | 需要@ | 范围 | 说明 |
|:-----:|:----:|:----:|:----:|
| httpcat + http status code | 否 | 群聊/私聊 | 后加http提示码 |
</details>

### 5.[Coin](https://github.com/ANGJustinl) | 昂昂Bot货币组件
<details>
WIP
</details>

## | 非原生插件 💕：

### 1.[chatgpt_on_qq](https://github.com/Suxmx/nonebot_plugin_chatgpt_on_qq) | 语言模型插件
<details>

## 配置项

所有 **必填** 为`否`的配置项，都可以不写进配置文件，如果这样做了，则这些配置项会取 **默认值**
中的内容，否则会取配置文件中写入的值，所以如果不清楚具体含义的可以直接不在配置文件中写入这些配置。

唯一 **必填** 的配置项只有 `api_key` ,如果你只有一个api_key，可以直接填写字符串，例如 `api_key="sk-xxx..."`
，如果你有多条key，可以填写字符串列表，例如 `api_key=["sk-xxx...", "sk-yyy...", "sk-zzz..."]`<br>
**注意：如果填写多条api key，配置文件中 `api_key = ["sk-xxx...", "sk-yyy...", "sk-zzz..."]` 最后一个key后面不能接逗号！
**<br>
**如果想要换行 在列表前后加上单引号！**<br>

```
api_key = '["sk-xxx...", 
 "sk-yyy...", "sk-zzz...",
 "sk-jjj..."]'
```

另外，如果在国内的话，代理虽然不是 **必填** 项，但是没有的话是无法连接到 openai
的，所以算是必填项，正向代理使用 `openai_proxy`
，例如 `openai_proxy="127.0.0.1:1080"` （前提是你有代理，这只是个例子）

`customize_prefix` 可以修改插件指令的公共前缀 默认是"/"，可以修改成别的，或者直接使用空字符串 `customize_prefix=""`
则去掉这个前缀，**建议设置为空字符串或者别的**

<details>
  <summary><b style="font-size: 1.2rem">部分非必填配置项介绍</b></summary>

`allow_private` 是否允许私聊触发插件

`at_sender` 回复是否@发送者

`key_load_balancing` 选项可以选择是否开启apikey的负载均衡，可以简单理解为是否每次从所有key中随机选一个进行使用，默认为否（即一直使用同一个
key 直到失效再切换下一个）<br>
因为据说同一个 ip 不能同时调用多个apikey，尤其是短时间调用量很大的情况（不过个人没有测试过），所以默认为关闭负载均衡。如果想开启可能代理软件也需要多
ip 负载均衡或者自己做ip池（大概…<br>
所以自己决定要不要开启吧~

`history_max` 和 `history_save_path` 是会话的全部历史记录，保存在本地；`chat_memory_max`
是会话与gpt交互时记忆的上下文最大聊天记录长度，实际上只是全部历史记录中的一部分，可以理解为他的记忆；

`preset_path` 是预设模板存放的文件夹，一般不需要改动

`default_only_admin` 群组默认会话管理权限状态，默认为所有人均可创建管理会话<br>
群组会话管理权限状态一共有两种：1、所有人均可以创建、管理会话；2、仅群主、管理员可以创建、管理会话，其余群员仅可加入对话<br>
可以使用 `/chat auth on` 与 `/chat auth off` 指令切换会话管理状态，具体用法见下方指令介绍

`change_chat_to` 可以修改 `chat系` 指令 中的 "chat" 为自定义字符串，因为电脑版qq /chat xxx
会被自动转换成表情，所以支持自定义。比如 `change_chat_to="Chat"` 就可以让 `/Chat list` 触发 `/chat list` 指令

`customize_talk_cmd` 可以修改 `talk` 指令 中 "talk" 为自定义字符，因为 如果将公共前缀置空的话，"talk"
字符串比较常见可能容易引发误触，可以修改成其他的 比如 `customize_talk_cmd="gpt"` 可以让 `/gpt` 触发 `/talk`

`auto_create_preset_info` 可以设置是否提示根据模板自动创建会话的信息，这条提示信息具体在用户不在任何会话时直接使用 `talk`
指令时触发，如果嫌太过频繁可以关闭。但只能关闭掉自动创建提示，主动创建会话仍旧有提醒。

</details>
<br>
<details>
  <summary><b style="font-size: 1.2rem">所有配置项表格</b></summary>

|           配置项           | 必填 | 类型            |        默认值         |                                   说明                                    |
|:-----------------------:|:--:|---------------|:------------------:|:-----------------------------------------------------------------------:|
|         api_key         | 是  | str/List[str] |                    |      填入你的api_key,类似"sk-xxx..."，支持多个key，以字符串列表形式填入，某个key失效后会自动切换下一个      |
|      allow_private      | 否  | bool          |        true        |                              插件是否支持私聊，默认开启                              |
|        at_sender        | 否  | bool          |        true        |                                回复是否@发送者                                 |                                 |
|       model_name        | 否  | str           |  "gpt-3.5-turbo"   |                             模型名称，具体可参考官方文档                              |
|      openai_proxy       | 否  | str           |        None        |                          正向HTTP代理 (HTTP PROXY)                          |
|         timeout         | 否  | int           |         10         |                                 超时时间（秒）                                 |
|     chat_memory_max     | 否  | int           |         10         |                          设置会话记忆上下文数量，填入大于2的数字                           |
|       history_max       | 否  | int           |        100         |                        设置保存的最大历史聊天记录长度，填入大于2的数字                         |
|    history_save_path    | 否  | str           | "data/ChatHistory" |                               设置会话记录保存路径                                |
|     openai_api_base     | 否  | str           |https://api.openai.com/v1|                          其他api地址/反向代理                                   |
|   key_load_balancing    | 否  | bool          |       false        |           是否启用apikey负载均衡，即每次使用不同的key访问，默认为关，即一直使用一个key直到失效再切换           |
|       temperature       | 否  | float         |        0.5         | 设置使用gpt的理智值(temperature)，介于0~2之间，较高值如`0.8`会使会话更加随机，较低值如`0.2`会使会话更加集中和确定 |
|       preset_path       | 否  | str           |   "data/Presets"   |                              填入自定义预设文件夹路径                               |
|   default_only_admin    | 否  | bool          |       false        |                       群组默认会话管理权限状态，默认为所有人均可创建管理会话                       |
|     change_chat_to      | 否  | str           |        None        |           因为电脑端的qq在输入/chat xxx时候经常被转换成表情，所以支持自定义指令前缀替换"chat"            |
|    customize_prefix     | 否  | str           |        "/"         |                   自定义命令前缀，不填默认为"/"，如果不想要前缀可以填入空字符串 ""                   |
|   customize_talk_cmd    | 否  | str           |       "talk"       |              自定义和GPT会话的命令后缀，为了防止在去除前缀情况下talk因为常见而误触发可以自定义               |
| auto_create_preset_info | 否  | bool          |        true        |          是否发送自动根据模板创建会话的信息，如果嫌烦可以关掉，不过只能关掉自动创建的提示，主动创建的会一直有提醒           |
|       max_tokens        | 否  | int           |        1024        |                              一次最大回复token数量                              |

</details>
<br>
<details>
  <summary><b style="font-size: 1.2rem">配置项示例</b></summary>

```
api_key=["sk-xxx...", "sk-yyy...", ...] # 最后一个key后面不要加逗号，另外如果要多行则列表前后加单引号，参考上方介绍
at_sender=true
key_load_balancing=false
model_name="gpt-3.5-turbo" # 默认为gpt-3.5-turbo，具体可参考官方文档
temperature=0.5 # 理智值，介于0~2之间
openai_proxy="x.x.x.x:xxxxx"
chat_memory_max=10 # 填入大于2的数字
history_max=100 # 填入大于2的数字
history_save_path="E:/Kawaii" # 填入你的历史会话保存文件夹路径，如果修改最好填绝对路径，不过一般不需要修改，可以直接删掉这一行
openai_api_base = "https://api.moonshot.cn/v1" # 其他api地址(需支持openai库) 如kimi / cloudflare workers，空字符串或留空都将不使用
timeout=10
preset_path="E:/Kitty" # 填入你的历史会话保存文件夹路径，如果修改最好填绝对路径，不过一般不需要修改，可以直接删掉这一行
allow_private=true # 是否允许私聊触发插件
default_only_admin=false
change_chat_to="Chat" # 具体效果见上方介绍，如果不需要修改也可以直接删掉这一行
customize_prefix="/" # 具体效果见上方介绍，如果不需要修改也可以直接删掉这一行
customize_talk_cmd="talk" # 具体效果见上方介绍，如果不需要修改也可以直接删掉这一行
auto_create_preset_info=false # 具体效果见上方介绍，如果不需要修改也可以直接删掉这一行
max_tokens=1024 # 具体效果见上方介绍，如果不需要修改也可以直接删掉这一行
```

</details>

## 基础指令

`/chat help` 获取指令帮助菜单<br>
`/chat auth` 获取当前群会话管理权限状态<br>
`/chat auth on` 设置当前群仅管理员可以管理会话<br>
`/chat auth off` 设置当前群所有人均可管理会话<br>
`/talk <会话内容>` 在当前会话中进行会话<br>

### 增

`/chat new`  根据预制模板prompt创建并加入一个新的会话<br>
`/chat new <自定义prompt>` 根据自定义prompt创建并加入一个新的会话<br>
`/chat json` 根据历史会话json来创建一个会话，输入该命令后会提示你在下一个消息中输入json<br>
`/chat cp` 根据当前会话创建并加入一个新的会话<br>
`/chat cp <id>` 根据会话<id>为模板进行复制新建加入（id为`/chat list`中的序号）<br>

### 删

`/chat del` 删除当前所在会话<br>
`/chat del <id>` 删除序号为<id>的会话（id为`/chat list`中的序号）<br>
`/chat clear` 清空本群全部会话<br>
`/chat clear <@user>` 删除@用户创建的会话<br>

### 改

`/chat join <id>` 加入会话（id为`/chat list`中的序号）<br>
`/chat rename <name>` 重命名当前会话<br>

### 查

`/chat who` 查看当前会话信息<br>
`/chat list` 获取当前群所有存在的会话的序号及创建时间<br>
`/chat list <@user>` 获取当前群查看@的用户创建的会话<br>
`/chat prompt` 查看当前会话的prompt<br>
`/chat dump` 导出当前会话json字符串格式的上下文信息，可以用于`/chat json`导入<br>
`/chat keys` 脱敏显示当前失效api key，仅主人


<details>
  <summary><b style="font-size: 1.2rem">指令表格</b></summary>

|           指令            |       权限        | 需要@ |   范围   |                    说明                     |
|:-----------------------:|:---------------:|:---:|:------:|:-----------------------------------------:|
|      `/chat help`       |       群员        |  否  | 私聊/群聊  |                 获取指令帮助菜单                  |
|      `/chat auth`       |       群员        |  否  |   群聊   |               获取当前群会话管理权限状态               |
|     `/chat auth on`     |    主人/群主/管理员    |  否  |   群聊   |              设置当前群仅管理员可以管理会话              |
|    `/chat auth off`     |    主人/群主/管理员    |  否  |   群聊   |              设置当前群所有人均可管理会话               |
|     `/talk <会话内容>`      |       群员        |  否  | 私聊/群聊  |                在当前会话中进行会话                 |
|       `/chat new`       |       群员        |  否  | 私聊/群聊  |          根据预制模板prompt创建并加入一个新的会话          |
| `/chat new <自定义prompt>` |       群员        |  否  | 私聊/群聊  |          根据自定义prompt创建并加入一个新的会话           |
|      `/chat json`       |       群员        |  否  | 私聊/群聊  | 根据历史会话json来创建一个会话，输入该命令后会提示你在下一个消息中输入json |
|       `/chat cp`        |       群员        |  否  | 私聊/群聊  |             根据当前会话创建并加入一个新的会话             |
|     `/chat cp <id>`     |       群员        |  否  | 私聊/群聊  | 根据会话<id>为模板进行复制新建加入（id为`/chat list`中的序号）  |
|       `/chat del`       | 主人/群主/管理员/会话创建人 |  否  | 私聊/群聊  |                 删除当前所在会话                  |
|    `/chat del <id>`     | 主人/群主/管理员/会话创建人 |  否  | 私聊/群聊  |     删除序号为<id>的会话（id为`/chat list`中的序号）     |
|      `/chat clear`      |    主人/群主/管理员    |  否  | 私聊/群聊  |                 清空本群全部会话                  |
|  `/chat clear <@user>`  | 主人/群主/管理员/会话创建人 |  否  | 私聊/群聊  |                删除@用户创建的会话                 |
|    `/chat join <id>`    |       群员        |  否  | 私聊/群聊  |         加入会话（id为`/chat list`中的序号）         |
|  `/chat rename <name>`  | 主人/群主/管理员/会话创建人 |  否  | 私聊/群聊  |                  重命名当前会话                  |
|       `/chat who`       |       群员        |  否  | 私聊/群聊  |                 查看当前会话信息                  |
|      `/chat list`       |       群员        |  否  | 私聊/群聊  |           获取当前群所有存在的会话的序号及创建时间            |
|  `/chat list <@user>`   |       群员        |  否  |   群聊   |             获取当前群查看@的用户创建的会话              |
|     `/chat prompt`      |       群员        |  否  | 私聊/群聊  |               查看当前会话的prompt               |
|      `/chat dump`       |       群员        |  否  | 私聊/群聊  | 导出当前会话json字符串格式的上下文信息，可以用于`/chat json`导入  |
|      `/chat keys`       |       主人        |  否  | 私聊 /群聊 |            脱敏显示当前失效api key，仅主人            |

</details>
</details>

### 2.[YetAnotherPicSearch](https://github.com/NekoAria/YetAnotherPicSearch) | 搜图插件

### 配置教程
<details>
   参照 [config.py](../YetAnotherPicSearch/config.py) 文件，更改 `.env.prod` 文件或 `.env` 文件 (都不存在就创建 `.env` 文件) 中的配置项，如：

    ```
    PROXY="http://127.0.0.1:1080"
    SAUCENAO_API_KEY=""
    ```

   其中：

   - `SAUCENAO_API_KEY` 必须配置，否则无法正常使用搜图功能。没有就申请一个：[先注册](https://saucenao.com/user.php)，然后到 [api 页面](https://saucenao.com/user.php?page=search-api) 复制。
   - 如果遇到各种奇怪的网络问题，请配置 `PROXY` ，如果是 socks 代理，要用"socks5://" 或 "socks4://" 的格式，具体取决于你的代理协议。
   - 如果 sauceNAO 的 API 使用触发当日上限，除非同时换新的 API Key 和代理节点，否则仅换其中一个没有意义。
   - 如果想要在 E-Hentai 标题搜索无结果时自动调用 NHentai 标题搜索，先用配置的 `PROXY` 做代理，通过浏览器访问 NHentai 来通过 CloudFlare 检测，然后配置通过检测的 UA 和 cookies 到 `nhentai_useragent` 和 `nhentai_cookies` 。
</details>

### 使用教程
<details>

#### 日常使用
- `搜图关键词` (`search_keyword`) 可以自定义，默认为 `搜图` ；之所以叫做关键词而不是指令，是因为它可以不在消息开头
- 如果想让机器人只响应含有 `搜图关键词` 的消息 (优先级高于 `search_immediately`) ，启用 `search_keyword_only`
- 私聊：
    - 发送 `搜图关键词` 及参数进入搜图模式，详见下方的 [搜图模式](#搜图模式)
    - 直接发送图片 (如果禁用了 `search_immediately` ，需要先发送 `搜图关键词` 进入搜图模式)
    - 回复自己或机器人发送的图片，在消息中附上 `搜图关键词` 及参数 (如果回复的是机器人，必须带上 `搜图关键词` 才会搜图，否则会被无视)
- 群聊：
    - 发送 `搜图关键词` 及参数进入搜图模式，详见下方的 `搜图模式`
    - `@机器人` 并发送图片
    - 回复某人 (包括自己) 发送的图片，在消息中附上 `搜图关键词` 或 `@机器人` 及参数 (如果回复的是机器人，必须带上 `搜图关键词` 才会搜图，否则会被无视)
- 可以在同一条消息中包含多张图片，会自动批量搜索
- 搜索图片时可以在消息内包含以下参数来指定搜索范围或者使用某项功能，优先级 (除去 `--purge`) 从上到下：
    - `--all` 全库搜索 (默认)
    - `--pixiv` 从 Pixiv 中搜索
    - `--danbooru` 从 Danbooru 中搜索
    - `--doujin` 搜索本子
    - `--anime` 搜索番剧
    - `--a2d` 使用 Ascii2D 进行搜索 (优势搜索局部图能力较强)
    - `--baidu` 使用 Baidu 进行搜索
    - `--ex` 使用 ExHentai (E-Hentai) 进行搜索
    - `--google` 使用 Google 进行搜索
    - `--iqdb` 使用 Iqdb 进行搜索
    - `--yandex` 使用 Yandex 进行搜索
    - `--purge` 无视缓存进行搜图，并更新缓存
- 对于 SauceNAO：
    - 如果得到的结果相似度低于 60% (可配置)，会自动使用 Ascii2D 进行搜索 (可配置)
    - 如果额度耗尽，会自动使用 Ascii2D 进行搜索
    - 如果搜索到本子，会自动在 ExHentai (E-Hentai) 中搜索并返回链接 (如果有汉化本会优先返回汉化本链接)
    - 如果搜到番剧，会自动使用 WhatAnime 搜索番剧详细信息：
        - AnimeDB 与 WhatAnime 的结果可能会不一致，是正常现象，毕竟这是两个不同的搜索引擎
        - 同时展示这两个搜索的目的是为了尽力得到你可能想要的识别结果
- 对于 ExHentai：
    - 如果没有配置 `EXHENTAI_COOKIES` ，会自动使用 `E-Hentai` 搜索 (如何获取 cookies 请参考 [PicImageSearch 文档](https://pic-image-search.kituin.fun/wiki/picimagesearch/E-hentai/DataStructure/#cookies%E8%8E%B7%E5%8F%96))
    - 不支持单色图片的搜索，例如黑白漫画，只推荐用于搜索 CG 、画集、图集、彩色漫画、彩色封面等
    - 如果没有配置 `superusers` ，不会显示搜索结果的收藏状态
- 关于进行搜索后未收到机器人回复的新消息的情况：  
  这可能是因为消息中包含的链接被列入黑名单，成了所谓的 `红链`。需通过查阅 gocqhttp 或其他上游端的日志，来确定哪个网站的域名被封禁了，然后参照 `config.py` 文件配置相应的配置项 `to_confuse_urls` 来规避。

#### 搜图模式

搜图模式存在的意义是方便手机用户在转发图片等不方便在消息中夹带 @ 或搜图参数的情况下指定搜索范围或者使用某项功能：

- 发送 `搜图关键词` 并附上搜索范围或者功能参数，如果没有指定，会使用默认设置 (即 `--all`)
- 此时你发出来的下一条消息中的图 (也就是一次性的) 会使用指定搜索范围或者使用某项功能
</details>