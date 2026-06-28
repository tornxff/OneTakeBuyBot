from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

TOKEN = "এখানে_তোমার_নতুন_BotFather_Token"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        ["📘 Facebook", "🎵 TikTok"],
        ["▶️ YouTube", "📷 Instagram"]
    ]

    reply_markup = ReplyKeyboardMarkup(keyboard, resize_keyboard=True)

    await update.message.reply_text(
        "👋 স্বাগতম!\n\nএকটি প্ল্যাটফর্ম নির্বাচন করুন:",
        reply_markup=reply_markup
    )

app = Application.builder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))

print("Bot Started...")
app.run_polling()
