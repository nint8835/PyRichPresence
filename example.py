import asyncio
import time
import sys

from pyrichpresence import DiscordRPC, RichPresenceStatus

# Create event loop
if sys.platform == "win32":
    loop = asyncio.ProactorEventLoop()
else:
    loop = asyncio.get_event_loop()

# Create RPC object for given app ID
rpc = DiscordRPC('424664573598105601', loop=loop)

# Create a status object to display
state = RichPresenceStatus()
state.details = "Testing PyRichPresence"
state.large_image_key = "pyrichpresence"
state.small_image_key = "pyrichpresence_small"
state.small_image_text = "I'm an image, but smaller!"
state.large_image_text = "I'm an image!"
state.start_timestamp = time.time()


async def run():
    # Connect to RPC
    await rpc.start()
    while True:
        # Update your status
        await rpc.send_rich_presence(state)
        await asyncio.sleep(20)

loop.run_until_complete(run())
