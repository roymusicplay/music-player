import logging
from MusicKen.modules.msg import Messages as tr
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
from MusicKen.config import SOURCE_CODE, ASSISTANT_NAME, PROJECT_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, BOT_USERNAME, OWNER, KENKAN
from MusicKen.helpers.decorators import authorized_users_only

logging.basicConfig(level=logging.INFO)


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited 
)
async def start_(client: Client, message: Message):
    await message.reply_sticker("CAACAgUAAxkBAAFF-KFg-jaEvlhu_kNknYQjxsuyDvp--AACjAMAAtpWSVeocCICILIfRSAE")
    await message.reply_text(
        f"""👋🏻 Hallo, Nama saya [{PROJECT_NAME}](https://telegra.ph/file/9bc0650d7f60d0618d815.jpg)
Dikekolah oleh {OWNER}
・✦▭▭▭▭✧◦✦◦✧▭▭▭▭✦ ・
☑️ Saya memiliki banyak fitur untuk anda yang suka lagu
🔘 Memutar lagu di group 
🔘 Memutar lagu di channel
🔘 Mendownload lagu
🔘 Mencari link youtube
・✦▭▭▭▭✧◦✦◦✧▭▭▭▭✦ ・
☑️ Klik tombol bantuan untuk informasi lebih lanjut
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚔️ 𝙃𝙀𝙇𝙋", callback_data = f"help+1"),
                    InlineKeyboardButton(
                        "𝙂𝙍𝙊𝙐𝙋 𝙈𝙀 𝘿𝘼𝙇𝙊 ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "👥 𝙂𝙍𝙊𝙐𝙋", url=f"https://t.me/{SUPPORT_GROUP}"), 
                    InlineKeyboardButton(
                        "𝘾𝙃𝘼𝙉𝙉𝙀𝙇📣", url="https://t.me/DOSTI_GROUP_1234")],
                [
                    InlineKeyboardButton("🌟 𝘽𝙊𝙏 𝙇𝙄𝙎𝙏🌟", url="https://t.me/MOVIE_CHANNEL_1234"),
                    InlineKeyboardButton("💵 ꜱᴀᴡᴇʀɴʏᴀ", url="https://trakteer.id/kenkansaja/tip")
                ]        
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_photo(
        photo=f"{KENKAN}",
        caption=f"""**🔴 {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = '🔵 𝙊𝙒𝙉𝙀𝙍', url = "t.me/abhinasroy")],
                    [InlineKeyboardButton(text = '👥 𝙂𝙍𝙊𝙐𝙋', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = '𝘾𝙃𝘼𝙉𝙉𝙀𝙇 📣', url="https://t.me/DOSTI_GROUP_1234")],
                    [InlineKeyboardButton("🌟 𝘽𝙊𝙏 𝙇𝙄𝙎𝙏 🌟", url="https://t.me/MOVIE_CHANNEL_1234"), InlineKeyboardButton("💵 ꜱᴀᴡᴇʀɴʏᴀ", url="https://trakteer.id/kenkansaja/tip")]
                ]
        ),
    )


@Client.on_message(filters.private & filters.incoming & filters.command(['help']))
def _help(client, message):
    client.send_message(chat_id = message.chat.id,
        text = tr.HELP_MSG[1],
        parse_mode="markdown",
        disable_web_page_preview=True,
        disable_notification=True,
        reply_markup = InlineKeyboardMarkup(map(1)),
        reply_to_message_id = message.message_id
    )

help_callback_filter = filters.create(lambda _, __, query: query.data.startswith('help+'))

@Client.on_callback_query(help_callback_filter)
def help_answer(client, callback_query):
    chat_id = callback_query.from_user.id
    disable_web_page_preview=True
    message_id = callback_query.message.message_id
    msg = int(callback_query.data.split('+')[1])
    client.edit_message_text(chat_id=chat_id,    message_id=message_id,
        text=tr.HELP_MSG[msg],    reply_markup=InlineKeyboardMarkup(map(msg))
    )


def map(pos):
    if pos==1:
        button = [
            [InlineKeyboardButton(text = '⬅️ Sebelummya', callback_data = "help+5"),
             InlineKeyboardButton(text = 'Selanjutnya ➡️', callback_data = "help+2")]
        ]
    elif pos==len(tr.HELP_MSG)-1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton(text = '⚔️ 𝙃𝙀𝙇𝙋', callback_data = f"help+1"),
             InlineKeyboardButton(text = '𝙂𝙍𝙊𝙐𝙋 𝙈𝙀 𝘿𝘼𝙇𝙊➕', url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = '👥 𝙂𝙍𝙊𝙐𝙋', url=f"https://t.me/{SUPPORT_GROUP}"),
             InlineKeyboardButton(text = '𝘾𝙃𝘼𝙉𝙉𝙀𝙇📣', url="https://t.me/DOSTI_GROUP_1234")],
            [InlineKeyboardButton("🌟 𝘽𝙊𝙏 𝙇𝙄𝙎𝙏 🌟", url="https://t.me/MOVIE_CHANNEL_1234"), InlineKeyboardButton("💵 ꜱᴀᴡᴇʀɴʏᴀ", url="https://trakteer.id/kenkansaja/tip")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = '⬅️ sᴇʙᴇʟᴜᴍɴʏᴀ', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'sᴇʟᴀɴᴊᴜᴛɴʏᴀ ➡️', callback_data = f"help+{pos+1}")
            ],
        ]
    return button

@Client.on_message(
    filters.command("reload")
    & filters.group
    & ~ filters.edited
)
@authorized_users_only
async def admincache(client, message: Message):
    await message.reply_photo(
      photo=f"{KENKAN}",
      caption="✅ **Bot berhasil dimulai ulang!**\n\n **Daftar admin telah diperbarui**",
      reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = '🔵 𝙊𝙒𝙉𝙀𝙍', url = "t.me/abhinasroy")],
                    [InlineKeyboardButton(text = '👥 𝙂𝙍𝙊𝙐𝙋', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = '𝘾𝙃𝘼𝙉𝙉𝙀𝙇📣', url="https://t.me/DOSTI_GROUP_1234")],
                    [InlineKeyboardButton("🌟 𝘽𝙊𝙏 𝙇𝙄𝙎𝙏 🌟", url="https://t.me/MOVIE_CHANNEL_1234"), InlineKeyboardButton("💵 ꜱᴀᴡᴇʀɴʏᴀ", url="https://trakteer.id/kenkansaja/tip")]
                ]
        ),
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """
**🔰 Perintah**
      
**=>> Memutar Lagu 🎧**
      
**=>> Playing Songs **
      
• /play (song name) - To Play the song you requested via youtube
• /ytplay (song name) - To Play the song you requested via youtube
• /yt (song name) - To Play the song you requested via youtube
• /p (song name) - To Play the song you requested via youtube
• /dplay (song name) - To Play the song you requested via deezer
• /splay (song name) - To Play the song you requested via jio saavn
• /player: Open the Player settings menu
• /skip: Skips the current track
• /pause: Pause track
• /resume: Resume a paused track
• /end: ​​Stops media playback
• /current: Displays the currently playing track
• /playlist: Displays a playlist
      
All Commands Can Be Used Except Command /player /skip /pause /resume /end Only For Group Admin
      
**==>>Download Song **
      
• /song [song name]: Download song audio from youtube
***=>> Music Play Channel **
      
️ Only for linked group admins:
      
• /cplay (song name) - play the song you requested
• /cdplay (song name) - play the song you requested via deezer
• /csplay (song name) - play the song you requested via jio saavn
• /cplaylist - Show currently playing list
• /cccurrent - Show currently playing
• /cplayer - open the music player settings panel
• /cpause - pause song playback
• /cresume - resume song playback
• /cskip - play next song
• /cend - stop music playing
• /userbotjoinchannel - invite assistants to your chat""",
      reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = '🔵 𝙊𝙒𝙉𝙀𝙍', url = "t.me/abhinasroy")],
                    [InlineKeyboardButton(text = '👥 𝙂𝙍𝙊𝙐𝙋', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = 𝘾𝙃𝘼𝙉𝙉𝙀𝙇 📣', url="https://t.me/DOSTI_GROUP_1234")],
                    [InlineKeyboardButton("🌟 𝘽𝙊𝙏 𝙇𝙄𝙎𝙏🌟", url="https://t.me/MOVIE_CHANNEL_1234"), InlineKeyboardButton("💵 ꜱᴀᴡᴇʀɴʏᴀ", url="https://trakteer.id/kenkansaja/tip")]
                ]
        ),
    )


