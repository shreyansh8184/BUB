from ub import app
from pyrogram import filters

from ub.bot.strings import (PAYMENT_DETAILS, HOW, COD, FORMAT)

@app.on_message(filters.command("start"))
async def start(client, message):
    name = message.from_user['first_name']
    user_id = message.from_user['id']
    mention =  [{name}](tg://user?id={user_id})
    await message.reply(START_TEXT)
    await app.send_message(message.chat_id, INFO)

@app.on_message(filters.incoming & filters.photo)
async def screenshot(client, message):
    await message.reply(MONEY_DEPOSITED)

