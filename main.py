'''
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
import threading
from flask import Flask
from pyrogram import Client, filters

app = Flask(__name__)
bot = Client("formatter_bot", api_id=25956970, api_hash="5fb73e6994d62ba1a7b8009991dd74b6", bot_token="7894175068:AAHjkgMb1SHXVysQpWJ_R3WUwIlUFFdVKw4")

@app.route('/')
def health_check():
    return "OK", 200

def run_flask():
    app.run(host="0.0.0.0", port=8000)

def run_bot():
    @bot.on_message(filters.private & filters.text)
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

    bot.run()

# Run both Flask server and bot concurrently
threading.Thread(target=run_flask).start()
run_bot()
'''
import logging
import threading
from flask import Flask
from pyrogram import Client, filters

# Logging configuration
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Health check server (Flask)
flask_app = Flask(__name__)

@flask_app.route('/')
def health_check():
    return "OK", 200

def run_flask():
    try:
        logger.info("Starting Flask health server on port 8000...")
        flask_app.run(host="0.0.0.0", port=8000)
    except Exception as e:
        logger.error(f"Flask server error: {e}")

# Telegram bot configuration
api_id = 25956970
api_hash = "5fb73e6994d62ba1a7b8009991dd74b6"
bot_token = "7894175068:AAHjkgMb1SHXVysQpWJ_R3WUwIlUFFdVKw4"

bot = Client("formatter_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@bot.on_message(filters.private & filters.text)
def format_anime_info(client, message):
    try:
        text = message.text
        lines = text.split("\n")

        if not lines or len(lines) < 2:
            raise ValueError("Not enough lines to parse")

        title_line = lines[0]
        episodes = "Unknown"
        synopsis = "Not provided."

        for i, line in enumerate(lines):
            if "ɴᴏ ᴏғ ᴇᴘɪsᴏᴅᴇs" in line.lower():
                episodes = line.split(":")[-1].strip()
            if "sʏɴᴏᴘsɪs" in line.lower():
                synopsis = "\n".join(lines[i:]).split(":", 1)[-1].strip()
                break

        output = f"""{title_line}
─────────────────────────────────────────────────────
➡ ꜱᴇᴀꜱᴏɴ : 01
➡ ʟᴀɴɢᴜᴀɢᴇ : ᴊᴀᴘ | ᴇɴɢ
➡ Qᴜᴀʟɪᴛʏ : 480ᴘ| 720ᴘ| 1080ᴘ
➡ ᴇᴘɪꜱᴏᴅᴇꜱ : {episodes}
⭐ sʏɴᴏᴘsɪs : {synopsis}
────────────────────────────────
👑ᴘᴏᴡᴇʀᴇᴅ ʙʏ : @Animes2u"""

        message.reply_text(output)

    except Exception as e:
        logger.error(f"Error parsing message: {e}")
        message.reply_text("❌ Failed to parse the input. Please check the format.")

def start_bot():
    try:
        logger.info("Starting Telegram bot...")
        bot.run()
    except Exception as e:
        logger.critical(f"Bot failed to start: {e}")

# Start both Flask and bot
if __name__ == "__main__":
    threading.Thread(target=run_flask, daemon=True).start()
    start_bot()
