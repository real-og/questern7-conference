from loader import dp
from aiogram import types
from aiogram.dispatcher import FSMContext
import texts


@dp.message_handler(commands=['start'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    await message.answer(texts.start_message)


@dp.message_handler(commands=['score'], state="*")
async def send_welcome(message: types.Message, state: FSMContext):
    if message.text == '/score':
        res = await texts.generate_all_scores()
    else:
        team_name = message.text.replace('/score ', '')
        res = await texts.generate_score_by_name(team_name)
    await message.answer(res)
