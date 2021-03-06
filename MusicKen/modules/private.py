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
        f"""ππ» Hallo, Nama saya [{PROJECT_NAME}](https://telegra.ph/file/9bc0650d7f60d0618d815.jpg)
Dikekolah oleh {OWNER}
γ»β¦β­β­β­β­β§β¦β¦β¦β§β­β­β­β­β¦ γ»
βοΈ Saya memiliki banyak fitur untuk anda yang suka lagu
π Memutar lagu di group 
π Memutar lagu di channel
π Mendownload lagu
π Mencari link youtube
γ»β¦β­β­β­β­β§β¦β¦β¦β§β­β­β­β­β¦ γ»
βοΈ Klik tombol bantuan untuk informasi lebih lanjut
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "βοΈ ππππ", callback_data = f"help+1"),
                    InlineKeyboardButton(
                        "πππππ ππ πΏπΌππ β", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
                [
                    InlineKeyboardButton(
                        "π₯ πππππ", url=f"https://t.me/{SUPPORT_GROUP}"), 
                    InlineKeyboardButton(
                        "πΎππΌπππππ£", url="https://t.me/DOSTI_GROUP_1234"),
                [
                    InlineKeyboardButton("π π½ππ πππππ", url="https://t.me/MOVIE_CHANNEL_1234"),
                    InlineKeyboardButton("π΅ κ±α΄α΄‘α΄ΚΙ΄Κα΄", url="https://trakteer.id/kenkansaja/tip")
                ]        
            ]
        ),
        reply_to_message_id=message.message_id
        )

@Client.on_message(filters.command("start") & ~filters.private & ~filters.channel)
async def gstart(_, message: Message):
    await message.reply_photo(
        photo=f"{KENKAN}",
        caption=f"""**π΄ {PROJECT_NAME} is online**""",
        reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = 'π΅ πππππ', url = "t.me/abhinasroy")],
                    [InlineKeyboardButton(text = 'π₯ πππππ', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = 'πΎππΌππππ π£', url="https://t.me/DOSTI_GROUP_1234"),
                    [InlineKeyboardButton("π π½ππ ππππ π", url="https://t.me/MOVIE_CHANNEL_1234"), InlineKeyboardButton("π΅ κ±α΄α΄‘α΄ΚΙ΄Κα΄", url="https://trakteer.id/kenkansaja/tip")]
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
            [InlineKeyboardButton(text = 'β¬οΈ Sebelummya', callback_data = "help+5"),
             InlineKeyboardButton(text = 'Selanjutnya β‘οΈ', callback_data = "help+2")]
        ]
    elif pos==len(tr.HELP_MSG)-1:
        url = f"https://t.me/{SUPPORT_GROUP}"
        button = [
            [InlineKeyboardButton(text = 'βοΈ ππππ', callback_data = f"help+1"),
             InlineKeyboardButton(text = 'πππππ ππ πΏπΌππβ', url=f"https://t.me/{BOT_USERNAME}?startgroup=true")],
            [InlineKeyboardButton(text = 'π₯ πππππ', url=f"https://t.me/{SUPPORT_GROUP}"),
             InlineKeyboardButton(text = 'πΎππΌπππππ£', url="https://t.me/DOSTI_GROUP_1234"),
            [InlineKeyboardButton("π π½ππ ππππ π", url="https://t.me/MOVIE_CHANNEL_1234"), InlineKeyboardButton("π΅ κ±α΄α΄‘α΄ΚΙ΄Κα΄", url="https://trakteer.id/kenkansaja/tip")]
        ]
    else:
        button = [
            [
                InlineKeyboardButton(text = 'β¬οΈ sα΄Κα΄Κα΄α΄Ι΄Κα΄', callback_data = f"help+{pos-1}"),
                InlineKeyboardButton(text = 'sα΄Κα΄Ι΄α΄α΄α΄Ι΄Κα΄ β‘οΈ', callback_data = f"help+{pos+1}")
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
      caption="β **Bot berhasil dimulai ulang!**\n\n **Daftar admin telah diperbarui**",
      reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = 'π΅ πππππ', url = "t.me/abhinasroy")],
                    [InlineKeyboardButton(text = 'π₯ πππππ', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = 'πΎππΌπππππ£', url="https://t.me/DOSTI_GROUP_1234"),
                    [InlineKeyboardButton("π π½ππ ππππ π", url="https://t.me/MOVIE_CHANNEL_1234"), InlineKeyboardButton("π΅ κ±α΄α΄‘α΄ΚΙ΄Κα΄", url="https://trakteer.id/kenkansaja/tip")]
                ]
        ),
    )

@Client.on_message(filters.command("help") & ~filters.private & ~filters.channel)
async def ghelp(_, message: Message):
    await message.reply_text(
        """
**π° Perintah**
      
**=>> Memutar Lagu π§**
      
**=>> Playing Songs **
      
β’ /play (song name) - To Play the song you requested via youtube
β’ /ytplay (song name) - To Play the song you requested via youtube
β’ /yt (song name) - To Play the song you requested via youtube
β’ /p (song name) - To Play the song you requested via youtube
β’ /dplay (song name) - To Play the song you requested via deezer
β’ /splay (song name) - To Play the song you requested via jio saavn
β’ /player: Open the Player settings menu
β’ /skip: Skips the current track
β’ /pause: Pause track
β’ /resume: Resume a paused track
β’ /end: ββStops media playback
β’ /current: Displays the currently playing track
β’ /playlist: Displays a playlist
      
All Commands Can Be Used Except Command /player /skip /pause /resume /end Only For Group Admin
      
**==>>Download Song **
      
β’ /song [song name]: Download song audio from youtube
***=>> Music Play Channel **
      
οΈ Only for linked group admins:
      
β’ /cplay (song name) - play the song you requested
β’ /cdplay (song name) - play the song you requested via deezer
β’ /csplay (song name) - play the song you requested via jio saavn
β’ /cplaylist - Show currently playing list
β’ /cccurrent - Show currently playing
β’ /cplayer - open the music player settings panel
β’ /cpause - pause song playback
β’ /cresume - resume song playback
β’ /cskip - play next song
β’ /cend - stop music playing
β’ /userbotjoinchannel - invite assistants to your chat""",
      reply_markup=InlineKeyboardMarkup(
                  [
                    [InlineKeyboardButton(text = 'π΅ πππππ', url = "t.me/abhinasroy")],
                    [InlineKeyboardButton(text = 'π₯ πππππ', url=f"https://t.me/{SUPPORT_GROUP}"),
                     InlineKeyboardButton(text = πΎππΌππππ π£', url="https://t.me/DOSTI_GROUP_1234"),
                    [InlineKeyboardButton("π π½ππ πππππ", url="https://t.me/MOVIE_CHANNEL_1234"), InlineKeyboardButton("π΅ κ±α΄α΄‘α΄ΚΙ΄Κα΄", url="https://trakteer.id/kenkansaja/tip")]
                ]
        ),
    )


