from aiogram import types

from tgbot_template.tgbot.keyboards.inline_funds.ikb_fourth_funds4 import ikb_fourth_type_first_fund, \
    ikb_fourth_type_second_fund, ikb_fourth_type_third_fund
from tgbot_template.tgbot.media.data import funsd


async def fourth_type_first_fund(call: types.CallbackQuery):
    text = funsd.get("fourth_fund_type").get("first_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fourth_type_first_fund)


async def fourth_type_second_fund(call: types.CallbackQuery):
    text = funsd.get("fourth_fund_type").get("second_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fourth_type_second_fund)


async def fourth_type_third_fund(call: types.CallbackQuery):
    text = funsd.get("fourth_fund_type").get("third_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fourth_type_third_fund)