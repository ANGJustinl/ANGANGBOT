import os
from datetime import datetime
from nonebot import get_plugin_config

from .config import Config
from .utils import get_daily_image

config = get_plugin_config(Config)

async def get_daily_image_scheduler():
    url = "https://v2.alapi.cn/api/zaobao"
    token = config.daily_news_api_key
    msg = await get_daily_image(url, token)
    print(type(msg))
    # Create directory if it doesn't exist
    os.makedirs("data/daily", exist_ok=True)

    # Get current date for the filename
    today = datetime.now().strftime("%Y-%m-%d")
    filepath = f"data/daily/{today}.txt"

    # Save the image to the file
    with open(filepath, "w") as f:
        f.write(msg)