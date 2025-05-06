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



