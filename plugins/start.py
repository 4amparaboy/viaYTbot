from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup

@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Bot news š¤©", url="https://t.me/DGUuz")],
        [InlineKeyboardButton(
            "Report Bugs š", url="https://t.me/president_tuychiyev")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>ā\nā»ļø Welcome to <b>@viaYTbot</b>\n\nšš¼ <a href='https://telegra.ph/More-info-01-09'>for More info</a> šš¼"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
