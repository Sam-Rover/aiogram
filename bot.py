from aiogram import Bot, types
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import Message
from config import token, admin_id

bot = Bot(token)
dp = Dispatcher(bot)

async def on_startup(_):
	print('Бот запущен')
	await bot.send_message(admin_id, 'bot started...')


# client

@dp.message_handler(commands=['start', 'help'])
async def command_start(message : Message):
	try:
		await bot.send_message(message.from_user.id, 'Приятного аппетита')
		await message.delete()
	except:
		await message.reply('start this bot @aiogrampycommand_bot')


@dp.message_handler(commands=['Режим_работы'])
async def time_work(message : Message):
	await message.reply('Пн - Пт с 9:00 до 18:00')


@dp.message_handler(commands=['Расположение'])
async def time_work(message : Message):
	await message.reply('Алмазарский район, ул. Карасарай, 314А')

# client


#common

# @dp.message_handler()
# async def new_echo(message : types.Message):

	# await message.answer(message.text)
	# await message.reply(message.text)
	# await bot.send_message(message.from_user.id, message.text)

executor.start_polling(dp, on_startup=on_startup)