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
to_channel = [-1001652625342,-1001643820163,-1001468059554,-1001120853598,-1001582997297,-1001514275764,-1001663802984,-1001529949759,-1001526995634,-1001525770536,-1001333978413,-1001239074731,-1001372997271,-1001457625038,-1001748493882,-1001593784776,-1001368695613,-1001445095452,-1001538321307,-1001517048806,-1001582900944,-1001480873177,-1001579175259]

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
