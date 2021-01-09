from pyrogram import Client, Filters
import time

admin_one = 677949397

@Client.on_message(Filters.command(["users"], ["ads"], ["cancel"]))
async def start(client, message):
    with open('sendik.txt', 'r') as cmd1:
        sendik = cmd1.read()
    if message.from_user.id == admin_one and message.text == "/users":
        with open('id_tg.txt', 'r') as fayl:
            users = str(len(fayl.readlines()))
            stattxt = f'All users: <b>{users}</b>'
        await message.reply_text(stattxt, parse_mode='html')
    elif message.from_user.id == admin_one and message.text == "/ads":
        with open('sendik.txt', 'w') as cmd2:
            cmd2.write("/sendik")
    elif message.from_user.id == admin_one and message.text == "/cancel":
        with open('sendik.txt', 'w') as cmd3:
            cmd3.write("/no")
            sendik = "/no"
    elif message.from_user.id == admin_one and sendik == "/sendik":
        with open('id_tg.txt', 'r') as arr:
            Lusers = arr.readlines()
        for i in Lusers:
            try:
                if message.content_type == "text":
                   # text
                    tex = message.html_text
                    await message.send_message(i, tex, parse_mode='html')
                    time.sleep(0.05)
                elif message.content_type == "photo":
                    # photo
                    capt = message.html_caption
                    photo = message.photo[-1].file_id
                    await message.send_photo(i, photo, caption=capt,
                                   parse_mode='html')
                    time.sleep(0.05)
                elif message.content_type == "video":
                    # video
                    capt = message.html_caption
                    photo = message.video.file_id
                    await message.send_video(i, photo, parse_mode='html')
                    time.sleep(0.05)
                elif message.content_type == "audio":
                    # audio
                    capt = message.html_caption
                    photo = message.audio.file_id
                    await message.send_audio(i, photo, caption=capt, parse_mode='html')
                    time.sleep(0.05)
                elif message.content_type == "voice":
                    # voice
                    capt = message.html_caption
                    photo = message.voice.file_id
                    await message.send_voice(i, photo, caption=capt,
                                   parse_mode='html')
                    time.sleep(0.05)
                elif message.content_type == "animation":
                    # animation
                    capt = message.html_caption
                    photo = message.animation.file_id
                    await message.send_animation(
                        i, photo, caption=capt, parse_mode='html')
                    await message.sleep(0.05)
                elif message.content_type == "document":
                    # document
                    capt = message.html_caption
                    photo = message.document.file_id
                    await message.send_document(i, photo, caption=capt,
                                      parse_mode='html')
                    time.sleep(0.05)
            except Exception as e:
                await message.send_message(admin_one, f"blocked: {str(e)}")
                time.sleep(0.05)
                pass
        await message.send_message(message.chat.id, "Habar yuborildi !")
        with open('sendik.txt', 'w') as wr_ok:
            wr_ok.write("/no")
