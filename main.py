'''
from pyrogram import Client, filters

api_id = 22648485  # Replace with your API ID
api_hash = "8a714c643f86acb3d07a2baa4831f95b"  # Replace with your API Hash
bot_token = "7926389008:AAE84r3NKMfPxttKXsVYZNUcEUj6OCZAEHA"  # Replace with your Bot Token

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

api_id = 22648485  # Replace with your API ID
api_hash = "8a714c643f86acb3d07a2baa4831f95b"  # Replace with your API Hash
bot_token = "7926389008:AAE84r3NKMfPxttKXsVYZNUcEUj6OCZAEHA"  # Replace with your Bot Token

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
# main.py
import os
import threading
import unicodedata
from pyrogram import Client, filters
from flask import Flask

# Telegram bot setup (unchanged)
api_id   = int(os.getenv("API_ID"))
api_hash = os.getenv("API_HASH")
bot_token= os.getenv("BOT_TOKEN")

app_bot = Client("formatter_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

def normalize_text(text):
    return ''.join(c for c in unicodedata.normalize('NFD', text)
                   if unicodedata.category(c) != 'Mn')

@app_bot.on_message(filters.private & filters.text)
def format_anime_info(client, message):
    text = normalize_text(message.text)
    lines = text.split("\n")
    title = lines[0]
    eps = synopsis = ""
    for l in lines:
        if "No of episodes" in l or "ɴᴏ ᴏғ ᴇᴘɪsᴏᴅᴇs" in l:
            eps = l.split(":",1)[1].strip()
        if "Synopsis" in l or "sʏɴᴏᴘsɪs" in l:
            synopsis = l.split(":",1)[1].strip()
            break
    out = f"""{title}
──────────────────────────────
➡ ꜱᴇᴀꜱᴏɴ : 01
➡ ʟᴀɴɢᴜᴀɢᴇ : ᴊᴀᴘ | ᴇɴɢ
➡ Qᴜᴀʟɪᴛʏ : 480ᴘ|720ᴘ|1080ᴘ
➡ ᴇᴘɪꜱᴏᴅᴇꜱ : {eps or 'N/A'}
⭐ sʏɴᴏᴘsɪs : {synopsis or 'N/A'}
──────────────────────────────
👑ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Animes2u"""
    message.reply_text(out)

def run_bot():
    app_bot.run()

# Minimal Flask app for health check on port 8000
web = Flask("health")

@web.route("/")
def health():
    return "OK", 200

if __name__ == "__main__":
    # Start Telegram bot in a background thread
    threading.Thread(target=run_bot).start()
    # Then start Flask on port 8000
    web.run(host="0.0.0.0", port=int(os.environ.get("PORT", 8000)))



