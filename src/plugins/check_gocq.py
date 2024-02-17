import asyncio
import nonebot
import subprocess

from nonebot.log import logger
from nonebot import require, on_command

group_id = None  # 这里填检测群位置


try:
    scheduler = require("nonebot_plugin_apscheduler")
    from nonebot_plugin_apscheduler import scheduler
except Exception:
    scheduler = None

logger.opt(colors=True).info(
    "已检测到软依赖<y>nonebot_plugin_apscheduler</y>, <g>开启gocq检测</g>"
    if scheduler
    else "未检测到软依赖<y>nonebot_plugin_apscheduler</y>，<r>禁用gocq检测</r>"
)

restart_qsign = on_command(
    "restart_qsign_bot1", aliases={"bot1_re"}, priority=5, block=True
)


async def qsign_livecheck():
    msg_ids = []
    try:
        msg_id = (
            await nonebot.get_bot().send_group_msg(
                group_id=688693279,
                message="bot存活检测中,若此条未撤回,则bot进行一次重启",
            )
        )["message_id"]
        msg_ids.append(msg_id)
        await asyncio.sleep(30)
        try:
            for msg_id in msg_ids:
                await nonebot.get_bot().delete_msg(message_id=msg_id)
        except:
            pass
    except Exception as e:
        try:
            subprocess.run(["docker", "restart", "qsign"])
            asyncio.sleep(30)
            await nonebot.get_bot().send_group_msg(
                group_id=688693279, message="重启,上次下线原因为: " + str(e)
            )
        except Exception:
            logger.critical("gocq出错")
            raise SystemExit


@restart_qsign.handle()
async def restarting_qsign():
    await qsign_livecheck()
    pass


if scheduler:
    scheduler.add_job(qsign_livecheck, "interval", hours=1, id="qsign1_livecheck")
