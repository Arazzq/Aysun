import os, logging, asyncio
from telethon import Button
from telethon import TelegramClient, events
from telethon.sessions import StringSession
from telethon.tl.types import ChannelParticipantsAdmins

logging.basicConfig(
    level=logging.INFO,
    format='%(name)s - [%(levelname)s] - %(message)s'
)
LOGGER = logging.getLogger(__name__)

api_id = int(os.environ.get("APP_ID"))
api_hash = os.environ.get("APP_HASH")
bot_token = os.environ.get("TOKEN")
client = TelegramClient('client', api_id, api_hash).start(bot_token=bot_token)

anlik_calisan = []


@client.on(events.NewMessage(pattern="^/start$"))
async def start(event):
  await event.reply("**Aysun Bot**, ",
                    buttons=(
                      [Button.url('🌟 Məni Bir Qrupa Sal', 'https://t.me/Ayssunbot?startgroup=a'),
                      Button.url('📣 Support', 'https://t.me/supmerlin'),
                      Button.url('👨‍💻 Sahibim', 'https://t.me/Arazdi')]
                    ),
                    link_preview=False
                   )
@client.on(events.NewMessage(pattern="^/help$"))
async def help(event):
  helptext = "**Aysun bot'un Yardım Menyusu**\n\nƏmr: Hələ əmrlər hazır deyil təəssüf ki, \nSağol..."
  await event.reply(helptext,
                    buttons=(
                      [Button.url('🌟 Məni qrupa sal', 'https://t.me/Ayssunbot?startgroup=a'),
                       Button.url('📣 Support', 'https://t.me/supmerlin'),
                      Button.url('👨‍💻 Sahibim', 'https://t.me/Arazdi')]
                    ),
            
print(">> Bot çalışıre ürəymm🚀 @ozuduqaqaw məlumat alabilərsən <<")
client.run_until_disconnected()
