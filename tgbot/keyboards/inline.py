from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from tgbot_template.tgbot.media.somelol import funsd

ikb_funds = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                     [
                                         InlineKeyboardButton(text=funsd.get("first_fund_type").get("type_name"),
                                                              callback_data=funsd.get("first_fund_type").get(
                                                                  "type_name")),
                                         InlineKeyboardButton(funsd.get("second_fund_type").get("type_name"),
                                                              callback_data=funsd.get("second_fund_type").get(
                                                                  "type_name")),

                                     ]
                                 ])

ikb_first_type_funds = InlineKeyboardMarkup(row_width=2,
                                            inline_keyboard=[
                                                [
                                                    InlineKeyboardButton(
                                                        text=funsd.get("first_fund_type").get("first_fund").get("name"),
                                                        callback_data=funsd.get("first_fund_type").get(
                                                            "first_fund").get("name")),
                                                    InlineKeyboardButton(
                                                        text=(funsd.get("first_fund_type").get("second_fund").get(
                                                            "name")),
                                                        callback_data=(
                                                            funsd.get("first_fund_type").get("second_fund").get(
                                                                "name"))),
                                                    InlineKeyboardButton(
                                                        text="обратно",
                                                        callback_data="stepback"),
                                                ]
                                              ]
                                            )

ikb_second_type_funds = InlineKeyboardMarkup(row_width=2,
                                             inline_keyboard=[
                                                 [
                                                     InlineKeyboardButton(
                                                         text=funsd.get("second_fund_type").get("first_fund").get(
                                                             "name"),
                                                         callback_data=funsd.get("second_fund_type").get(
                                                             "first_fund").get(
                                                             "name")),
                                                     InlineKeyboardButton(
                                                         text=funsd.get("second_fund_type").get("second_fund").get(
                                                             "name"),
                                                         callback_data=funsd.get("second_fund_type").get(
                                                             "second_fund").get(
                                                             "name")),
                                                 ]
                                             ])

ikb_fist_type_first_fund = InlineKeyboardMarkup(row_width=2,
                                                inline_keyboard=[
                                                    [
                                                        InlineKeyboardButton(
                                                            text=funsd.get("first_fund_type").get("first_fund").get(
                                                                "info"),
                                                            callback_data="lol"),
                                                    ]
                                                ])

ikb_fist_type_second_fund = InlineKeyboardMarkup(row_width=2,
                                                 inline_keyboard=[
                                                     [
                                                         InlineKeyboardButton(
                                                             text=funsd.get("first_fund_type").get("second_fund").get(
                                                                 "info"),
                                                             callback_data="lol"),
                                                     ]
                                                 ])

ikb_second_type_first_fund = InlineKeyboardMarkup(row_width=2,
                                                  inline_keyboard=[
                                                      [
                                                          InlineKeyboardButton(
                                                              text=funsd.get("second_fund_type").get("first_fund").get(
                                                                  "info"),
                                                              callback_data="lol"), ]
                                                  ])

ikb_second_type_second_fund = InlineKeyboardMarkup(row_width=2,
                                                   inline_keyboard=[
                                                       [
                                                           InlineKeyboardButton(
                                                               text=funsd.get("second_fund_type").get(
                                                                   "second_fund").get("info"),
                                                               callback_data="lol"), ]
                                                   ])


