# Асинхронное скачивание картинок\файлов с любого сайта из https://thisxdoesnotexist.com/
# Сделать питоновский скрипт, которому можно указать количество файлов,
# которые нужно получить в нужную папку. Использовать aiohttp.
import asyncio
import sys
import time

import aiohttp

url = "https://thiscatdoesnotexist.com/"


async def run_easy():
    count = int(sys.argv[1])
    async with aiohttp.ClientSession() as session:
        for i in range(count):
            async with session.get(url) as response:
                with open(f"artifacts/easy/{i}.png", "bw") as file:
                    file.write((await response.content.read()))
            # Images on the site are updated once every second.
            # Could be removed, then adjacent images sometimes will be repeated
            time.sleep(1)

loop = asyncio.get_event_loop()
loop.run_until_complete(run_easy())
