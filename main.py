
from pyrogram import Client, filters

api_id = 25956970  # Replace with your API ID
api_hash = "5fb73e6994d62ba1a7b8009991dd74b6"  # Replace with your API Hash
bot_token = "7894175068:AAHjkgMb1SHXVysQpWJ_R3WUwIlUFFdVKw4"  # Replace with your Bot Token

app = Client("formatter_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)


@app.on_message(filters.private & filters.text)
def format_anime_info(client, message):
    text = message.text

    try:
        lines = text.split("\n")
        title_line = lines[0]
        episodes = ""
        synopsis = ""

        for line in lines:
            if "ɴᴏ ᴏғ ᴇᴘɪsᴏᴅᴇs" in line:
                episodes = line.split(":")[-1].strip()
            if "sʏɴᴏᴘsɪs" in line:
                synopsis_index = lines.index(line)
                synopsis = "\n".join(lines[synopsis_index:]).split(":", 1)[-1].strip()
                break

        output = f"""{title_line}
─────────────────────────────────────────────────────
➡ ꜱᴇᴀꜱᴏɴ : 01
➡ ʟᴀɴɢᴜᴀɢᴇ : ᴊᴀᴘ | ᴇɴɢ
➡ Qᴜᴀʟɪᴛʏ : 480ᴘ| 720ᴘ| 1080ᴘ
➡ ᴇᴘɪꜱᴏᴅᴇꜱ :{episodes}
⭐ sʏɴᴏᴘsɪs : {synopsis}
────────────────────────────────
👑ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Animes2u"""

        message.reply_text(output)

    except Exception as e:
        message.reply_text("❌ Failed to parse the input. Please check the format.")


app.run()

'''
'''
from pyrogram import Client, filters
import unicodedata

api_id = 22648485  # Replace with your API ID
api_hash = "8a714c643f86acb3d07a2baa4831f95b"  # Replace with your API Hash
bot_token = "7894175068:AAHjkgMb1SHXVysQpWJ_R3WUwIlUFFdVKw4"  # Replace with your Bot Token

app = Client("formatter_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def normalize_text(text):
    """Normalize the text to remove any weird formatting and make it easier to parse."""
    return ''.join([c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'])

@app.on_message(filters.private & filters.text)
def format_anime_info(client, message):
    text = message.text

    try:
        # Normalize input text to handle all font types
        text = normalize_text(text)

        lines = text.split("\n")
        title_line = lines[0]
        episodes = ""
        synopsis = ""

        for line in lines:
            if "ɴᴏ ᴏғ ᴇᴘɪsᴏᴅᴇs" in line:
                episodes = line.split(":")[-1].strip()
            if "sʏɴᴏᴘsɪs" in line:
                synopsis_index = lines.index(line)
                synopsis = "\n".join(lines[synopsis_index:]).split(":", 1)[-1].strip()
                break

        output = f"""{title_line}
─────────────────────────────────────────────────────
➡ ꜱᴇᴀꜱᴏɴ : 01
➡ ʟᴀɴɢᴜᴀɢᴇ : ᴊᴀᴘ | ᴇɴɢ
➡ Qᴜᴀʟɪᴛʏ : 480ᴘ| 720ᴘ| 1080ᴘ
➡ ᴇᴘɪꜱᴏᴅᴇꜱ :{episodes}
⭐ sʏɴᴏᴘsɪs : {synopsis}
────────────────────────────────
👑ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Animes2u"""

        message.reply_text(output)

    except Exception as e:
        message.reply_text(f"❌ Failed to parse the input. Please check the format.\nError: {e}")


app.run()
'''
'''
from pyrogram import Client, filters
import unicodedata

api_id = 25956970  # Replace with your API ID
api_hash = "5fb73e6994d62ba1a7b8009991dd74b6"  # Replace with your API Hash
bot_token = "7894175068:AAHjkgMb1SHXVysQpWJ_R3WUwIlUFFdVKw4"  # Replace with your Bot Token

app = Client("formatter_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def normalize_text(text):
    """Normalize the text to remove any weird formatting and make it easier to parse."""
    # This removes combining characters that could result in strange formats
    return ''.join([c for c in unicodedata.normalize('NFD', text) if unicodedata.category(c) != 'Mn'])

@app.on_message(filters.private & filters.text)
def format_anime_info(client, message):
    text = message.text

    try:
        # Normalize input text to handle all font types
        text = normalize_text(text)

        lines = text.split("\n")
        title_line = lines[0]
        episodes = ""
        synopsis = ""

        for line in lines:
            if "ɴᴏ ᴏғ ᴇᴘɪsᴏᴅᴇs" in line:
                episodes = line.split(":")[-1].strip()
            if "sʏɴᴏᴘsɪs" in line:
                synopsis_index = lines.index(line)
                synopsis = "\n".join(lines[synopsis_index:]).split(":", 1)[-1].strip()
                break

        output = f"""{title_line}
─────────────────────────────────────────────────────
➡ ꜱᴇᴀꜱᴏɴ : 01
➡ ʟᴀɴɢᴜᴀɢᴇ : ᴊᴀᴘ | ᴇɴɢ
➡ Qᴜᴀʟɪᴛʏ : 480ᴘ| 720ᴘ| 1080ᴘ
➡ ᴇᴘɪꜱᴏᴅᴇꜱ :{episodes}
⭐ sʏɴᴏᴘsɪs : {synopsis}
────────────────────────────────
👑ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Animes2u"""

        message.reply_text(output)

    except Exception as e:
        message.reply_text(f"❌ Failed to parse the input. Please check the format.\nError: {e}")


app.run()
'''
'''
import os
import threading
import unicodedata
from pyrogram import Client, filters
from flask import Flask

# ——— Your credentials ———
api_id    = 25956970   # Your API ID
api_hash  = "5fb73e6994d62ba1a7b8009991dd74b6"  # Your API Hash
bot_token = "7894175068:AAHjkgMb1SHXVysQpWJ_R3WUwIlUFFdVKw4"  # Your Bot Token
# ————————————————————

# Initialize Pyrogram bot
app_bot = Client("formatter_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def normalize_text(text):
    """Normalize the text to remove any weird formatting and make it easier to parse."""
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')

@app_bot.on_message(filters.private & filters.text)
def format_anime_info(client, message):
    text = normalize_text(message.text)
    lines = text.split("\n")
    title_line = lines[0].strip()
    episodes = ""
    synopsis = ""

    for line in lines:
        if "ɴᴏ ᴏғ ᴇᴘɪsᴏᴅᴇs" in line:
            episodes = line.split(":", 1)[1].strip()
        if "sʏɴᴏᴘsɪs" in line:
            synopsis = line.split(":", 1)[1].strip()
            break

    output = f"""{title_line}
─────────────────────────────────────────────────────
➡ ꜱᴇᴀꜱᴏɴ : 01
➡ ʟᴀɴɢᴜᴀɢᴇ : ᴊᴀᴘ | ᴇɴɢ
➡ Qᴜᴀʟɪᴛʏ : 480ᴘ| 720ᴘ| 1080ᴘ
➡ ᴇᴘɪꜱᴏᴅᴇꜱ : {episodes or 'N/A'}
⭐ sʏɴᴏᴘsɪs : {synopsis or 'N/A'}
────────────────────────────────
👑ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Animes2u"""
    message.reply_text(output)

def run_bot():
    app_bot.run()

# Flask health‑check app
web = Flask("health")

@web.route("/")
def health():
    return "OK", 200

if __name__ == "__main__":
    # 1) Start Telegram bot in background thread
    threading.Thread(target=run_bot, daemon=True).start()
    # 2) Serve HTTP health check on PORT (default 8000)
    web.run(host="0.0.0.0", port=int(os.getenv("PORT", 8000)))
'''
