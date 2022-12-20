from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from aiogram.utils.callback_data import CallbackData

from tgbot_template.tgbot.media.data import funsd

stepback_button = InlineKeyboardButton(text="Обратно", callback_data="обратно")

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




ikb_third_type_funds = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("third_fund_type").get("first_fund").get("name"),
                                                        callback_data=funsd.get("third_fund_type").get("first_fund").get("name")),
                                                ],
                                                [
                                                    stepback_button,
                                                ]]
                                            )
