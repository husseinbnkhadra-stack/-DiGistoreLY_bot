import asyncio
from telegram.ext import ApplicationBuilder, CommandHandler

# ... (8529951592:AAH8ToZc__XkiCV8AKAke5vOYM1yM4SVqPE) ...

async def main():
    # تأكد من وضع التوكن الخاص بك هنا أو استخدام المتغير البيئي
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("البوت يعمل الآن...")
    await app.run_polling()

if __name__ == '__main__':
    # هذا السطر يحل مشكلة await outside function
    asyncio.run(main())