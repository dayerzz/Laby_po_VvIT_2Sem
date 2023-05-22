import telebot
from tg_bot_code import cfg
from week import curr_week_for_bd, curr_week
from select_db import get_day_formatting, get_week_formatting

token = '6005198804:AAFQjwD24g6b9ULFWb-WCs5LtPqMvT0n_2g'
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start_bot(message):
    bot.send_message(message.chat.id, text="Здравствуйте, " + message.from_user.first_name + "!" + "😁\n"
                                           "Я - ваш персональный "
                                           "помощник, который отображает расписание МТУСИ" 
                                           "для вашей группы. Чтобы узнать, какие команды я могу выполнять, напишите "
                                           "команду /help или выберете её в меню!"
                     .format(message.from_user))



@bot.message_handler(commands=['help'])
def help_bot(message):
    bot.send_message(message.chat.id, text=cfg.help_txt)


@bot.message_handler(commands=['week'])
def help_bot(message):
    bot.send_message(message.chat.id, text=f'На данный момент {curr_week()} неделя')


@bot.message_handler(commands=['mtuci'])
def help_bot(message):
    bot.send_message(message.chat.id, text='Сайт МТУСИ: https://mtuci.ru')


@bot.message_handler(commands=['mon'])
def mon(message):
    if curr_week() == "ЧЁТНАЯ":
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(0), 1))}')
    else:
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(1), 1))}')


@bot.message_handler(commands=['tue'])
def mon(message):
    if curr_week() == "ЧЁТНАЯ":
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(0), 2))}')
    else:
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(1), 2))}')


@bot.message_handler(commands=['wed'])
def mon(message):
    if curr_week() == "ЧЁТНАЯ":
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(0), 3))}')
    else:
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(1), 3))}')


@bot.message_handler(commands=['thu'])
def mon(message):
    if curr_week() == "ЧЁТНАЯ":
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(0), 4))}')
    else:
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(1), 4))}')


@bot.message_handler(commands=['fr'])
def mon(message):
    if curr_week() == "ЧЁТНАЯ":
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(0), 5))}')
    else:
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(1), 5))}')


@bot.message_handler(commands=['sat'])
def mon(message):
    if curr_week() == "ЧЁТНАЯ":
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(0), 6))}')
    else:
        bot.send_message(message.chat.id, text=f'{(get_day_formatting(curr_week_for_bd(1), 6))}')


@bot.message_handler(commands=['curwk'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{(get_week_formatting(curr_week_for_bd(1)))}')


@bot.message_handler(commands=['nxtwk'])
def mon(message):
    bot.send_message(message.chat.id, text=f'{(get_week_formatting(curr_week_for_bd(0)))}')


@bot.message_handler(content_types=['text'])
def text(message):
    bot.send_message(message.chat.id, text='Ой, такой команды не существует!☹️\n'
                                           'Воспользуйтесь командой \n/help, чтобы узнать список команд, '
                                           'которые я могу выполнить.')


bot.polling(none_stop=True, interval=0)
