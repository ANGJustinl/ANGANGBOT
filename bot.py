import nonebot
from nonebot import require
from nonebot.log import logger
from nonebot.adapters.onebot.v11 import Adapter as ONEBOT_V11Adapter


nonebot.init()

driver = nonebot.get_driver()
driver.register_adapter(ONEBOT_V11Adapter)


nonebot.load_from_toml("pyproject.toml")
nonebot.load_plugins("src/plugins")


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

if __name__ == "__main__":
    nonebot.run()