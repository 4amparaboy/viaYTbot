from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    # write id and usernames
    with open('./id_tg.txt', 'r') as f1:
        idlar = f1.readlines()
    f1.close()

    if f'{message.chat.id}\n' not in idlar:
        with open('./id_tg.txt', 'a') as f2:
            f2.write(f'{message.chat.id}\n')
        await message.reply_text("yozildi")
        

    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bot news 🤩", url="https://t.me/DGUuz")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/president_tuychiyev")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>❕\n♻️ Welcome to <b>@viaYTbot</b>\n\n👉🏼 <a href='https://telegra.ph/More-info-01-09'>for More info</a> 👈🏼"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
