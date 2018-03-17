import asyncio
import sys

from pyrichpresence import DiscordRPC

loop = asyncio.ProactorEventLoop()
rpc = DiscordRPC('424664573598105601', loop=loop, verbose=True)


async def run():
    await rpc.start()
    while True:
        await rpc.send_rich_presence({
            'details': "Testing PyRichPresence",
            'state': f"{sys.platform}, {sys.version}"
        })
        await asyncio.sleep(1)

loop.run_until_complete(run())
