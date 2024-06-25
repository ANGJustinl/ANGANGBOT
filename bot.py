import nonebot
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter


nonebot.init()
app = nonebot.get_asgi()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)

nonebot.load_builtin_plugins("echo")

nonebot.load_plugin("nonebot_plugin_pixivbot")
nonebot.load_plugin("nonebot_plugin_tarot")
#nonebot.load_plugin('nonebot_plugin_fortune')
nonebot.load_plugin("nonebot_plugin_PicMenu")
nonebot.load_plugin("nonebot_plugin_weather_lite")



logger.success(
    "\n"
    "   #    #     #  #####     #    #     #  #####  ######  ####### ####### \n"
    "  # #   ##    # #     #   # #   ##    # #     # #     # #     #    #    \n"
    " #   #  # #   # #        #   #  # #   # #       #     # #     #    #    \n"
    "#     # #  #  # #  #### #     # #  #  # #  #### ######  #     #    #    \n"
    "####### #   # # #     # ####### #   # # #     # #     # #     #    #    \n"
    "#     # #    ## #     # #     # #    ## #     # #     # #     #    #    \n"
    "#     # #     #  #####  #     # #     #  #####  ######  #######    #    \n"
    "昂昂bot部署成功"
)

nonebot.load_from_toml("pyproject.toml")

if __name__ == "__main__":
    nonebot.run(app="__mp_main__:app", access_log=False)
