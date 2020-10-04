from ub import app
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup
from pyrogram.types import InlineKeyboardButton
from pyrogram.types import CallbackQuery

from ub.bot.strings import (INFO, MONEY_DEPOSITED, NOTED, DEPOSIT, RELEASED, REPORT, RELEASED, REPORTED)

@app.on_callback_query()
async def report(client, callback_query):
          if callback_query.data == "answer":
              await callback_query.edit_message_text(DEPOSIT)
              return
          else:
            await callback_query.edit_message_text(REPORT)


@app.on_message(filters.command("report"))
async def rep(client, message):
    await message.reply(REPORTED)

@app.on_message(filters.command("release"))
async def release(client, message):
    await message.reply(RELEASED)

@app.on_message(filters.command("start"))
async def start(client, message):
    name = message.from_user['first_name']
    user_id = message.from_user['id']
    mention = f"[{name}](tg://user?id={user_id})"
    START_TEXT = START_TEXT = f"Hello {mention} I Hope You Are Fine. This is Telegram's Official Escrow Bot Made For Safety Against Carders And Scammers."
    await message.reply(START_TEXT)
    keyboard = InlineKeyboardMarkup([[InlineKeyboardButton(text="Deposit", callback_data=r"answer"), InlineKeyboardButton(text="Report", callback_data=r"report")]])
    await app.send_message(message.chat.id, INFO, reply_markup=keyboard)

@app.on_message(filters.incoming & filters.photo)
async def screenshot(client, message):
    await message.reply(MONEY_DEPOSITED)


@app.on_message(filters.incoming & filters.text)
async def msg(client, message):
    text = message.text
    if text.startswith("@"):
       await message.reply(NOTED)


