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


ikb_second_type_funds = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("second_fund_type").get("first_fund").get("name"),
                                                        callback_data=funsd.get("second_fund_type").get(
                                                            "first_fund").get("name")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("second_fund_type").get("second_fund").get(
                                                            "name")),
                                                        callback_data=(
                                                            funsd.get("second_fund_type").get("second_fund").get(
                                                                "name"))),
                                                ],
[
                                                    InlineKeyboardButton(
                                                        text=funsd.get("second_fund_type").get("third_fund").get("name"),
                                                        callback_data=funsd.get("second_fund_type").get(
                                                            "third_fund").get("name")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("second_fund_type").get("fourth_fund").get(
                                                            "name")),
                                                        callback_data=(
                                                            funsd.get("second_fund_type").get("fourth_fund").get(
                                                                "name"))),
                                                ],

                                                [
                                                    stepback_button,
                                                ]
                                            ])

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
# ikb_fourth_type_funds = InlineKeyboardMarkup(row_width=2,
#                                             inline_keyboard=[
#                                                 [
#                                                     InlineKeyboardButton(
#                                                         text=funsd.get("fourth_fund_type").get("first_fund").get("name"),
#                                                         callback_data=funsd.get("fourth_fund_type").get(
#                                                             "first_fund").get("name")),
#                                                     InlineKeyboardButton(
#                                                         text=funsd.get("fourth_fund_type").get("second_fund").get("name"),
#                                                         callback_data=funsd.get("third_fund_type").get("second_fund").get("name"))
#                                                 ],
                                                # [
                                                #     InlineKeyboardButton(
                                                #         text=funsd.get("fourth_fund_type").get("third_fund").get(
                                                #             "name"),
                                                #         callback_data=funsd.get("fourth_fund_type").get(
                                                #             "third_fund").get("name")),
                                                # ],
                                                # [
                                                #     InlineKeyboardButton(text="Обратно",
                                                #                          callback_data="stepback"),
                                                # ]])


ikb_second_type_first_fund = InlineKeyboardMarkup(row_width=2,
                                                  inline_keyboard=[
                                                      [
                                                          InlineKeyboardButton(
                                                              text=funsd.get("second_fund_type").get("first_fund").get(
                                                                  "name"),
                                                              url=funsd.get("second_fund_type").get("first_fund").get(
                                                                  "site"))],
                                                      [
                                                          stepback_button,
                                                      ]
                                                  ])

ikb_second_type_second_fund = InlineKeyboardMarkup(row_width=2,
                                                   inline_keyboard=[
                                                       [
                                                           InlineKeyboardButton(
                                                               text=funsd.get("second_fund_type").get(
                                                                   "second_fund").get("name"),
                                                               url=funsd.get("second_fund_type").get("second_fund").get(
                                                                   "site"))],
                                                       [
                                                           stepback_button,
                                                       ]
                                                   ])
