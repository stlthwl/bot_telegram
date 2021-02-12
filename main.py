import telebot
from telebot import types
from telebot.types import InputMediaPhoto


bot = telebot.TeleBot('TOKEN')   #Ваш токен, который вы получили от BotFather
markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
name = ''
phone = ''
specialist = ''
promotion_name = ''
promotion_phone = ''


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row('Цены и услуги', 'Записаться')
    markup.row('Акции', 'О нас')
    bot.send_message(message.chat.id, 'Добро пожаловать в MONSTUDIO - студию маникюра и педикюра!💅🏻',
                     reply_markup=markup)
    bot.send_message(message.chat.id, 'Здесь Вы сможете:\n'
                                      '\n- ознакомиться с ценами и услугами;\n'
                                      '- ознакомиться с примерами работ наших мастеров;\n'
                                      '- отслеживать актуальные акции и предложения;\n'
                                      '- получить купон на скидку при записи.\n'
                                      '\nЧтобы узнать интересующую Вас информацию, выберите нужный раздел, пользуясь '
                                      'подсказками ниже👇🏻', reply_markup=markup)
    bot.register_next_step_handler(message, section_selection)


def section_selection(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Цены и услуги':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, prices_and_services)
    elif message.text == 'Записаться':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.from_user.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, sign_up)
    elif message.text == 'Акции':
        markup.row('Записаться по акции')
        markup.row('В начало')
        bot.send_message(message.chat.id, '🔥Акция🔥\nЗнакомство с мастером Евгенией.\nУспейте записаться на маникюр с '
                                          'покрытием всего за 990руб!\n\nВнимание!!!\nЗапись по акционной цене и '
                                          'купоны на скидку не суммируются', reply_markup=markup)
        bot.register_next_step_handler(message, promotion_sign_up)
    elif message.text == 'О нас':
        markup.row('Контакты', 'Примеры работ')
        bot.send_message(message.from_user.id, 'Уютная студия маникюра в центре города Домодедово.\nНаши специалисты - '
                                               'настоящие мастера своего дела!\nОказываем качественные услуги и даем '
                                               'гарантию на наши работы.\nКомфортная зона ожидания, чай, кофе, WI-FI, '
                                               'ТВ.\nМы ценим своих клиентов и делаем все, чтобы Вы были довольны!'
                                               '\nЖдем Вас у нас в студии😊', reply_markup=markup)
        bot.register_next_step_handler(message, info)
    else:
        markup.row('В начало')
        bot.send_message(message.chat.id, 'Для продолжения работы воспользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, start)


def prices_and_services(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Ногтевой сервис':
        markup.row('Записаться')
        markup.row('Вернуться назад')
        markup.row('В начало')
        with open('nailprice.jpg', 'rb') as price_nails:  # Отправка картинки с прайсом
            data = price_nails.read()
        bot.send_photo(message.from_user.id, photo=data)
        bot.send_message(message.from_user.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, sign_from)
    elif message.text == 'Брови':
        markup.row('Записаться')
        markup.row('Вернуться назад')
        markup.row('В начало')
        browprice = open('browprice.jpg', 'rb')  # Отправка картинки с прайсом
        bot.send_photo(message.chat.id, browprice)
        bot.send_message(message.from_user.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, sign_from2)
    else:
        markup.row('В начало')
        bot.send_message(message.chat.id, 'Для общения со мной пользуйтесь встроенной клавиатурой👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, start)


def sign_up(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Ногтевой сервис':
        markup.row('Светлана', 'Елена')
        markup.row('Евгения')
        bot.send_message(message.from_user.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Брови':
        markup.row('Татьяна')
        bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    else:
        markup.row('В начало')
        bot.send_message(message.chat.id, 'Для общения со мной пользуйтесь встроенной клавиатурой👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, start)


def specialists(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup()
    global specialist
    specialist = message.text
    if (message.text == 'Светлана') or (message.text == 'Записаться к Светлане'):
        markup.row('Подтвердить запись')
        markup.row('Вернуться назад')
        markup.row('В начало')
        svetka = open('sveta.jpg', 'rb')  # отправка фото мастера
        bot.send_photo(message.chat.id, svetka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻 @****',
                                             url='https://www.instagram.com/')  # инлайн клавиатура с ссылкой на инстаграм
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp: +7968*******', reply_markup=keyboard)  # сообщение с номером телефона мастера
        bot.send_message(message.chat.id, 'Подтвердите запись, чтобы получить купон на скидку😊', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_sing_up)
    elif (message.text == 'Елена') or (message.text == 'Записаться к Елене'):
        markup.row('Подтвердить запись')
        markup.row('Вернуться назад')
        markup.row('В начало')
        lenka = open('lena.jpeg', 'rb')
        bot.send_photo(message.chat.id, lenka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻 @****',
                                             url='https://www.instagram.com/')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp: +7926*******', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Подтвердите запись, чтобы получить купон на скидку😊', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_sing_up)
    elif (message.text == 'Евгения') or (message.text == 'Записпться к Евгении') or (message.text == 'Записаться по акции'):
        markup.row('Подтвердить запись')
        markup.row('Вернуться назад')
        markup.row('В начало')
        zhenka = open('zhenya.jpeg', 'rb')
        bot.send_photo(message.chat.id, zhenka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻@****',
                                             url='https://www.instagram.com/')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+7968*******\n+7926*******', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Подтвердите запись, чтобы получить купон на скидку😊', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_sing_up)
    elif (message.text == 'Татьяна') or (message.text == 'Записаться к Татьяне'):
        markup.row('Подтвердить запись')
        markup.row('Вернуться назад')
        markup.row('В начало')
        tanka = open('phototanya.jpeg', 'rb')
        bot.send_photo(message.chat.id, tanka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻@****',
                                             url='https://www.instagram.com/')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+7968*******\n+7926*******', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Подтвердите запись, чтобы получить купон на скидку😊', reply_markup=markup)
        bot.register_next_step_handler(message, confirm_sing_up)
    elif message.text == 'Вернуться назад':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, info_about_master)
    elif message.text == 'В начало':
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def confirm_sing_up(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    if message.text == 'Подтвердить запись':
        markup = types.ReplyKeyboardRemove(selective=False)  # встроенная клавиатура неактивна после однократного нажатия
        msg = bot.send_message(message.chat.id, 'Введите имя', reply_markup=markup)
        bot.register_next_step_handler(msg, reg_name)
    elif message.text == 'Вернуться назад':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, sign_up)
    elif message.text == 'В начало':
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def promotion_sign_up(message):
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup()
    if message.text == 'Записаться по акции':
        markup = types.ReplyKeyboardRemove(selective=False)
        zhenka = open('zhenya.jpeg', 'rb')
        bot.send_photo(message.chat.id, zhenka)
        url_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻@****',
                                             url='https://www.instagram.com/')
        keyboard.add(url_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+7968*******\n+7926*******', reply_markup=keyboard)
        bot.send_message(message.chat.id, 'Введите имя: ', reply_markup=markup)
        bot.register_next_step_handler(message, promotion_reg_name)
    elif message.text == 'В начало':
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def sign_from(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Записаться':
        markup.row('Светлана', 'Елена')
        markup.row('Евгения')
        bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Вернуться назад':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, prices_and_services)
    elif message.text == 'В начало':
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def sign_from2(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Записаться':
        markup.row('Татьяна')
        bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Вернуться назад':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, prices_and_services)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def reg_name(message):
    global name
    name = message.text
    bot.send_message(message.from_user.id, 'Введите номер Вашего телефона')
    bot.register_next_step_handler(message, reg_phone)


def promotion_reg_name(message):
    global promotion_name
    promotion_name = message.text
    bot.send_message(message.from_user.id, 'Введите номер Вашего телефона')
    bot.register_next_step_handler(message, promotion_reg_phone)


def reg_phone(message):
    global phone
    phone = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='yes')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='no')
    keyboard.add(key_no)
    confirm = 'Имя: ' + str(name) + '\nТелефон: ' + str(phone) + '\nВерно?'
    bot.send_message(message.from_user.id, text=confirm, reply_markup=keyboard)


def promotion_reg_phone(message):
    global promotion_phone
    promotion_phone = message.text
    keyboard = types.InlineKeyboardMarkup()
    key_yes = types.InlineKeyboardButton(text='Да', callback_data='correct')
    keyboard.add(key_yes)
    key_no = types.InlineKeyboardButton(text='Нет', callback_data='incorrect')
    keyboard.add(key_no)
    confirm = 'Имя: ' + str(promotion_name) + '\nТелефон: ' + str(promotion_phone) + '\nВерно?'
    bot.send_message(message.from_user.id, text=confirm, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if call.data == "yes":
        global name
        global phone
        global specialist
        markup.row('Получить купон')
        confirm = 'Новая запись!\n' + 'К мастеру: ' + str(specialist) + '\nИмя: ' + str(name) + '\nТелефон: ' + str(phone)
        msg = bot.send_message(call.message.chat.id, 'Заявка успешно отправлена!\nВ ближайшее время наш специалист с '
                                                     'Вами свяжется.\nБлагодарим за уделенное время и'
                                                     ' дарим Вам купон на скидку!', reply_markup=markup)
        bot.send_message(chat_id=-1, text=confirm)  # ID группы или пользователя, куда нужно пересылать сообщения о записи
                                                    # !!! ID должен быть со знаком "-" !!!
        bot.register_next_step_handler(msg, coupon)
    elif call.data == 'correct':
        global promotion_name
        global promotion_phone
        markup.row('В начало')
        confirm = 'Новая запись!\n' + 'Акция: знакомство с мастером\n' + 'Имя: ' + str(promotion_name) + '\nТелефон: ' + str(promotion_phone)
        msg = bot.send_message(call.message.chat.id, 'Заявка успешно отправлена!\nВ ближайшее время наш специалист с '
                                                     'Вами свяжется.\nБлагодарим за уделенное время!', reply_markup=markup)
        bot.send_message(chat_id=-1, text=confirm)
        bot.register_next_step_handler(msg, back_or_finish)
    elif call.data == "no":
        bot.send_message(call.message.chat.id, 'Повторите попытку\nВведите имя')
        bot.register_next_step_handler(call.message, reg_name)
    elif call.data == "incorrect":
        bot.send_message(call.message.chat.id, 'Повторите попытку\nВведите имя')
        bot.register_next_step_handler(call.message, promotion_reg_name)


def coupon(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Получить купон':
        markup.row('В начало')
        kup = open('coupon.jpeg', 'rb')
        bot.send_photo(message.chat.id, kup)
        bot.send_message(message.chat.id, 'Чтобы получить скидку, покажите купон мастеру', reply_markup=markup)
        bot.register_next_step_handler(message, back_or_finish)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def info(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard = types.InlineKeyboardMarkup()
    if message.text == 'Контакты':
        markup.row('Вернуться назад')
        markup.row('В начало')
        adres_btn = types.InlineKeyboardButton(text='Адрес: г. Домодедово, ****',
                                               url='url адрес метки на карте')
        keyboard.add(adres_btn)
        insta_btn = types.InlineKeyboardButton(text='ссылка на Instagram 👉🏻@****',
                                               url='https://www.instagram.com/')
        keyboard.add(insta_btn)
        bot.send_message(message.chat.id, 'Telegram, WhatsApp:\n+7968*******\n+7926*******', reply_markup=keyboard)
        bot.send_message(message.from_user.id, 'Связаться с нами можно по любому из указанных '
                                               'выше номеров, а так же с помощью Instagram', reply_markup=markup)
        bot.register_next_step_handler(message, back_or_finish)
    elif message.text == 'Примеры работ':
        markup.row('Ногтевой сервис', 'Брови')
        bot.send_message(message.chat.id, 'Выберите категорию', reply_markup=markup)
        bot.register_next_step_handler(message, info_about_master)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def info_about_master(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Ногтевой сервис':
        markup.row('Светлана', 'Елена')
        markup.row('Евгения')
        bot.send_message(message.from_user.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, info_photo)
    elif message.text == 'Брови':
        markup.row('Татьяна')
        bot.send_message(message.chat.id, 'Выберите мастера', reply_markup=markup)
        bot.register_next_step_handler(message, info_photo)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def info_photo(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Светлана':
        markup.row('Записаться к Светлане')
        markup.row('Вернуться назад')
        markup.row('В начало')
        ph1 = open('pic1.jpeg', 'rb')  # отправка нескольких фото в одном сообщении
        ph2 = open('pic2.jpeg', 'rb')  # !!! отправить за один раз можно не более 10 фотографий !!!
        ph3 = open('pic3.jpeg', 'rb')
        ph4 = open('pic4.jpeg', 'rb')
        ph5 = open('pic5.jpeg', 'rb')
        ph6 = open('pic6.jpeg', 'rb')
        ph7 = open('pic7.jpeg', 'rb')
        ph8 = open('pic8.jpeg', 'rb')
        ph9 = open('pic9.jpeg', 'rb')
        ph10 = open('pic10.jpeg', 'rb')
        media = [InputMediaPhoto(ph1), InputMediaPhoto(ph2), InputMediaPhoto(ph3), InputMediaPhoto(ph4),
				 InputMediaPhoto(ph5),
				 InputMediaPhoto(ph6), InputMediaPhoto(ph7), InputMediaPhoto(ph8), InputMediaPhoto(ph9),
				 InputMediaPhoto(ph10)]
        bot.send_media_group(message.chat.id, media)
        bot.send_message(message.chat.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Елена':
        markup.row('Записаться к Елене')
        markup.row('Вернуться назад')
        markup.row('В начало')
        le1 = open('l1.jpeg', 'rb')
        le2 = open('l2.jpeg', 'rb')
        le3 = open('l3.jpeg', 'rb')
        le4 = open('l4.jpeg', 'rb')
        le5 = open('l5.jpeg', 'rb')
        le6 = open('l6.jpeg', 'rb')
        le7 = open('l7.jpeg', 'rb')
        le8 = open('l8.jpeg', 'rb')
        le9 = open('l9.jpeg', 'rb')
        le10 = open('l10.jpeg', 'rb')
        lmedia = [InputMediaPhoto(le1), InputMediaPhoto(le2), InputMediaPhoto(le3), InputMediaPhoto(le4), InputMediaPhoto(le5),
				  InputMediaPhoto(le6), InputMediaPhoto(le7), InputMediaPhoto(le8), InputMediaPhoto(le9), InputMediaPhoto(le10)]
        bot.send_media_group(message.chat.id, lmedia)
        bot.send_message(message.chat.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Евгения':
        markup.row('Записаться к Евгении')
        markup.row('Вернуться назад')
        markup.row('В начало')
        zh1 = open('z1.jpeg', 'rb')
        zh2 = open('z2.jpeg', 'rb')
        zh3	= open('z3.jpeg', 'rb')
        zh4 = open('z4.jpeg', 'rb')
        zh5 = open('z5.jpeg', 'rb')
        zh6 = open('z6.jpeg', 'rb')
        zh7 = open('z7.jpeg', 'rb')
        zh8 = open('z8.jpeg', 'rb')
        zh9 = open('z9.jpeg', 'rb')
        zh10 = open('z10.jpeg', 'rb')
        zmedia = [InputMediaPhoto(zh1), InputMediaPhoto(zh2), InputMediaPhoto(zh3), InputMediaPhoto(zh4),
								  InputMediaPhoto(zh5), InputMediaPhoto(zh6), InputMediaPhoto(zh7),
								  InputMediaPhoto(zh8),InputMediaPhoto(zh9), InputMediaPhoto(zh10)]
        bot.send_media_group(message.chat.id, zmedia)
        bot.send_message(message.chat.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    elif message.text == 'Татьяна':
        markup.row('Записаться к Татьяне')
        markup.row('Вернуться назад')
        markup.row('В начало')
        br1 = open('im1.jpeg', 'rb')
        br2 = open('im2.jpeg', 'rb')
        br3 = open('im3.jpeg', 'rb')
        br4 = open('im4.jpeg', 'rb')
        br5 = open('im5.jpeg', 'rb')
        br6 = open('im6.jpeg', 'rb')
        br7 = open('im7.jpeg', 'rb')
        tmedia = [InputMediaPhoto(br1), InputMediaPhoto(br2), InputMediaPhoto(br3), InputMediaPhoto(br4),
				  InputMediaPhoto(br5), InputMediaPhoto(br6), InputMediaPhoto(br7)]
        bot.send_media_group(message.chat.id, tmedia)
        bot.send_message(message.chat.id, 'Хотите записаться?', reply_markup=markup)
        bot.register_next_step_handler(message, specialists)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Для продолжения работы пользуйтесь встроенной клавиатурой👇🏻',
                         reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


def back_or_finish(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    if message.text == 'Вернуться назад':
        markup.row('Контакты', 'Примеры работ')
        bot.send_message(message.from_user.id, 'Выберите подраздел', reply_markup=markup)
        bot.register_next_step_handler(message, info)
    else:
        markup.row('Цены и услуги', 'Записаться')
        markup.row('Акции', 'О нас')
        bot.send_message(message.chat.id, 'Выберите раздел👇🏻', reply_markup=markup)
        bot.register_next_step_handler(message, section_selection)


bot.polling(none_stop=True)
