from aiogram import types

from tgbot_template.tgbot.keyboards.inline_funds.ikb_first_funds import ikb_fist_type_first_fund, \
    ikb_fist_type_second_fund, ikb_fist_type_third_fund, ikb_fist_type_fourth_fund, ikb_fist_type_fifth_fund, \
    ikb_fist_type_sixth_fund, ikb_fist_type_seventh_fund, ikb_fist_type_eighth_fund
from tgbot_template.tgbot.media.data import funsd


async def fist_type_first_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("first_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_first_fund)


async def fist_type_second_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("second_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_second_fund)


async def fist_type_third_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("third_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_third_fund)


async def fist_type_fourth_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("fourth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_fourth_fund)


async def fist_type_fifth_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("fifth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_fifth_fund)


async def fist_type_sixth_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("sixth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_sixth_fund)


async def fist_type_seventh_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("seventh_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_seventh_fund)


async def fist_type_eighth_fund(call: types.CallbackQuery):
    text = funsd.get("first_fund_type").get("eighth_fund").get("info")
    await call.message.answer(text=text, reply_markup=ikb_fist_type_eighth_fund)