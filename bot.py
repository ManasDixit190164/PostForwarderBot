import time
import asyncio
from telethon import TelegramClient, events

print("Starting deployment...")

API_ID = 14295855
API_HASH = 'd7c97d558577a8633485c557a41174ef'
BOT_TOKEN = '2016904177:AAE0mbhWrI2aqzcQ_eNIhA_ozYuEzurgESc'
from_channel = -1001385076818
to_channel = [-1001748962108,-1001580614214,-1001708941209,-1001327205395,-1001777475205,-1001512412400,-1001589958093,-1001338840720,-1001643820163,-1001468059554,-1001120853598,-1001582997297,-1001529949759,-1001333978413,-1001593784776,-1001368695613,-1001445095452,-1001538321307,-100151704880,-1001582900944,-1001579175259]
bot = TelegramClient('bot', api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(incoming=True, chats=from_channel))
async def _(event):
    for i in to_channel:
        time.sleep(0.2)
        try:
            await bot.send_message(
                i,
                event.message
            )
        except Exception as e:
            print(e)


print("Bot has been deployed.")
bot.run_until_disconnected()
