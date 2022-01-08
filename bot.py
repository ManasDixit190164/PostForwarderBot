from os import environ
import os
import logging
import time
import asyncio
from telethon import TelegramClient, events, Button
from telethon.tl.functions.users import GetFullUserRequest

print("Starting deployment...")

API_ID = environ.get('API_ID', '14295855')
API_HASH = environ.get('API_HASH', 'd7c97d558577a8633485c557a41174ef')
BOT_TOKEN = '2016904177:AAE0mbhWrI2aqzcQ_eNIhA_ozYuEzurgESc'
from_channel = -1001385076818
to_channel = [-1001580614214]
bot = TelegramClient('bot', api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)


@bot.on(events.NewMessage(incoming=True, chats=from_channel))
async def _(event):
    #if not event.is_private:
    for i in to_channel:
        try:
            #for i in to_channel:
                time.sleep(0.2)
                if event.poll:
                    return
                if event.photo:
                    photo = event.media.photo
                    await bot.send_file(i, photo, caption=event.text, link_preview=False)
                elif event.media:
                    try:
                        if event.media.webpage:
                            await bot.send_message(i, event.text, link_preview=False)
                            return
                    except:
                        media = event.media.document
                        await bot.send_file(i, media, caption=event.text, link_preview=False)
                        return
                else:
                    await bot.send_message(i, event.text, link_preview=False)

        except Exception as e:
            print("ERROR : "+str(e))
            continue

print("Bot has been deployed.")
bot.run_until_disconnected()
