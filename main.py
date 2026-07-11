import os
from aiogram import Bot, Dispatcher, executor, types
from aiohttp import web

API_TOKEN = '8529951592:AAGWQD_kvwKnI2lPWAP1ulKGZe6OtPsYhB0'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

async def handle(request):
    return web.Response(text="Bot is running!")

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.answer("أهلاً بك في متجر ALNiSi! البوت يعمل الآن.")

if __name__ == '__main__':
    app = web.Application()
    app.router.add_get('/', handle)
    
    import asyncio
    loop = asyncio.get_event_loop()
    runner = web.AppRunner(app)
    loop.run_until_complete(runner.setup())
    site = web.TCPSite(runner, '0.0.0.0', int(os.environ.get('PORT', 10000)))
    loop.run_until_complete(site.start())
    
    executor.start_polling(dp, skip_updates=True)
