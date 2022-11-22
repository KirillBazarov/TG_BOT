from aiogram import types, Dispatcher
from aiogram.dispatcher import FSMContext
from aiogram.utils.markdown import hcode
from tgbot_template.tgbot.keyboards.inline import ikb_funds, ikb_fundi_Onkologia, ikb_fundi_UKR, ikb_fund_Onkologia_1, ikb_fund_Onkologia_2,ikb_fund_UKR_1,ikb_fund_UKR_2
type_dikt = {
    1: "Онкология",
    "funds_Onkologia": {"first_fund": "ВЕРА",
                        "second_fund": "ЖИВОЙ"},
    "third_fund": "AdVita",
    2: "Украина",
    "funds_UKR": {"first_fund": "первый",
                  "second_fund": "второй"},
    "third_fund": "третий",
}

async def vibor_tipa_funda(message: types.Message):
    text = [
        "Бот покажет куда ты можешь задонить.Вот пару направлений",
    ]
    await message.answer('\n'.join(text),reply_markup=ikb_funds)


async def vibor_funda_Onkologia(call: types.CallbackQuery):
    text = [
        f"так ты выбрал направление {type_dikt.get(1)}, теперь выбирем сам фонд",
    ]
    await call.message.answer('\n'.join(text), reply_markup=ikb_fundi_Onkologia)

async def vibor_funda_UKR(call: types.CallbackQuery):
    text = [
        f"так ты выбрал тнаправлению {type_dikt.get(2)}, теперь выбирем сам фонд",
    ]
    await call.message.answer('\n'.join(text), reply_markup=ikb_fundi_UKR)

async def fund_Onkologia_first(call: types.CallbackQuery):
    text = [
        f"ты выбрал фонд " + type_dikt["funds_Onkologia"]["first_fund"] + " инфа по нему",
    ]
    await call.message.answer('\n'.join(text), reply_markup=ikb_fund_Onkologia_1)

async def fund_Onkologia_second(call: types.CallbackQuery):
    text = [
        "ты выбрал фонд фот инфа по нему",
    ]
    await call.message.answer('\n'.join(text), reply_markup=ikb_fund_Onkologia_2)

async def fund_UKR_1(call: types.CallbackQuery):
    text = [
        "ты выбрал фонд фот инфа по нему",
    ]
    await call.message.answer('\n'.join(text), reply_markup=ikb_fund_UKR_1)

async def fund_UKR_2(call: types.CallbackQuery):
    text = [
        "ты выбрал фонд фот инфа по нему",
    ]
    await call.message.answer('\n'.join(text), reply_markup=ikb_fund_UKR_2)


def register_echo(dp: Dispatcher):
    dp.register_message_handler(vibor_tipa_funda, commands="form")
    dp.register_callback_query_handler(vibor_funda_Onkologia,text="Онкология")
    # dp.register_callback_query_handler(fund_Onkologia_1, text="фонд 1 анкология")
    # dp.register_callback_query_handler(fund_Onkologia_2, text="фонд 2 анкология")
    dp.register_callback_query_handler(vibor_funda_UKR, text="Украина")
    dp.register_callback_query_handler(fund_UKR_1, text="фонд 1 Украина")
    dp.register_callback_query_handler(fund_UKR_2, text="фонд 2 Украина")

