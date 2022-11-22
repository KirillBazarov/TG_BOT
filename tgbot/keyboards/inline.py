from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

type_dikt = {
    1: "Онкология",
    "funds_Onkologia": {"first_fund": "первый для онко ",
                        "second_fund": "Второй для онко"},
    "third_fund": "AdVita",
    2: "Украина",
    "funds_UKR": {"first_fund": "первый для ук",
                  "second_fund": "второй для ук"},
    "third_fund": "третий",
}


ikb_funds = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text="Онкологический",
                                                              callback_data="Онкология"),
                                         InlineKeyboardButton(text="Украина", callback_data="Украина"),
                                     ]
                                 ])

ikb_fundi_Onkologia = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text=type_dikt.get("funds_Onkologia").get("first_fund"),
                                                              callback_data=type_dikt.get("funds_Onkologia").get("first_fund")),
                                         InlineKeyboardButton(text=type_dikt.get("funds_Onkologia").get("second_fund"), callback_data=type_dikt.get("funds_Onkologia").get("second_fund")),
                                     ]
                                 ])

ikb_fundi_UKR = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text=type_dikt.get("funds_UKR").get("first_fund"),
                                                              callback_data=type_dikt.get("funds_UKR").get("first_fund")),
                                         InlineKeyboardButton(text=type_dikt.get("funds_UKR").get("second_fund"), callback_data=type_dikt.get("funds_UKR").get("second_fund")),
                                     ]
                                 ])

 # нужно поменять колбеки
ikb_fund_Onkologia_1 = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text=type_dikt.get("funds_Onkologia").get("first_fund"),
                                                              callback_data=type_dikt.get()),
                                     ]
                                 ])

ikb_fund_Onkologia_2 = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text=type_dikt.get("funds_Onkologia").get("second_fund"),
                                                              callback_data="инфа по фонду 1_2"),
                                     ]
                                 ])

ikb_fund_UKR_1 = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text=type_dikt.get("funds_UKR").get("first_fund"),
                                                              callback_data="инфа по фонду 2_1"),
                                     ]
                                 ])

ikb_fund_UKR_2 = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text=type_dikt.get("funds_UKR").get("second_fund"),
                                                              callback_data="инфа по фонду 2_2"),
                                     ]
                                 ])