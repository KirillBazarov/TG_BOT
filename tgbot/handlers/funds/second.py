from aiogram import types

from tgbot_template.tgbot.keyboards.inline_funds.ikb_second_funds import ikb_second_type_first_fund, \
    ikb_second_type_second_fund, ikb_second_type_third_fund, ikb_second_type_fourth_fund
from tgbot_template.tgbot.media.data import funsd

async def second_type_first_fund(call: types.CallbackQuery):
    text = funsd.get("second_fund_type").get("first_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_second_type_first_fund)


async def second_type_second_fund(call: types.CallbackQuery):
    text = funsd.get("second_fund_type").get("second_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_second_type_second_fund)


async def second_type_third_fund(call: types.CallbackQuery):
    text = funsd.get("second_fund_type").get("third_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_second_type_third_fund)


async def second_type_fourth_fund(call: types.CallbackQuery):
    text = funsd.get("second_fund_type").get("fourth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_second_type_fourth_fund)
