# Daisyxmusic (Telegram bot project )
# Copyright (C) 2021  Inukaasith 

# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.

# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton

from config import BOT_NAME as bn


@Client.on_message(filters.command("start") & filters.private & ~filters.channel)
async def start(_, message: Message):
    await message.reply_text(
        f"""Hello 👋! I can play music in Telegram Group voice chat.\n\n✣ Do you want me to play music in your Telegram group voice chat? Please click \'📜 Guide to Using BOT 📜\' button below to find out how to use mine.\n\n✣ Add it [Assistant Bimal](https://t.me/amsmusicbot) to your group to play music in your group voice chat.\n\nManaged With ☕️ By [Userbot plugin](https://t.me/AMSuserbot)""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "📜 Guide to Using BOT 📜", url="https://telegra.ph/Help-05-06")
                  ],[
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/AMSuserbot"
                    ),
                    InlineKeyboardButton(
                        "Channel", url="https://t.me/animemusicstash"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Music Player Is Online Now**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Support", url="https://t.me/AMSuserbot"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/AMSuserbot"
                    )
                ]
            ]
        )
   )

@Client.on_message(filters.command("reload") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
      await message.reply_text("""✅ **Music Player Is Online Now**""",
      reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Group Support", url="https://t.me/AMSuserbot"
                    ),
                    InlineKeyboardButton(
                        "Owner", url="https://t.me/AMSuserbot"
                    )
                ]
            ]
        )
   )


@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_text(
        """**Click the button below to see the guide to using a bot**""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "📜 Click the button below to see the guide to using a bot 📜", url="https://telegra.ph/Help-05-06"
                    )
                ]
            ]
        ),
    )
