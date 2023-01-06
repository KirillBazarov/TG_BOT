from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

from tgbot_template.tgbot.media.data import funsd


ikb_funds = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[[

                                     InlineKeyboardButton(text=funsd.get("first_fund_type").get("type_name"),
                                                          callback_data=funsd.get("first_fund_type").get(
                                                              "type_name")),
                                     InlineKeyboardButton(funsd.get("second_fund_type").get("type_name"),
                                                          callback_data=funsd.get("second_fund_type").get(
                                                              "type_name")),

                                 ], [
                                     InlineKeyboardButton(text=funsd.get("third_fund_type").get("type_name"),
                                                          callback_data=funsd.get("third_fund_type").get(
                                                              "type_name")),
                                     InlineKeyboardButton(funsd.get("fourth_fund_type").get("type_name"),
                                                          callback_data=funsd.get("fourth_fund_type").get(
                                                              "type_name")),

                                 ]])
