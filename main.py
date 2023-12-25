import random
import telebot
import nltk
from nltk.stem import WordNetLemmatizer
import webbrowser
from telebot import types










# Считываю свой токен из файла mytoken.txt, в твоем случае это будет не нужно
# Пример: bot = telebot.TeleBot('62732:RyJidSDIdi...')
mytoken = '6968654275:AAHBzuCwUhUmjasgaoJEzBYcl--5vO2rAWw'
# Передаем сюда токен, который получили от FatherBot
bot = telebot.TeleBot('6968654275:AAHBzuCwUhUmjasgaoJEzBYcl--5vO2rAWw')
# Варианты ответов пользователю, если тот ввел непонятное боту сообщение
answers = ['Я не понял, что ты хочешь сказать.', 'Извини, я тебя не понимаю.', 'Я не знаю такой команды.', 'Мой разработчик не говорил, что отвечать в такой ситуации... >_<']

# Обработка команды /start
@bot.message_handler(commands=['start'])
def welcome(message):
    # Добавляем кнопки, которые будут появляться после ввода команды /start
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🛍 Товары')
    button5 = types.KeyboardButton('⭐ Отзывы')
    button3 = types.KeyboardButton('📄 Справка')
    button4 = types.KeyboardButton('⁉ FAQ')
    # Разделяю кнопки по строкам так, чтобы товары были отдельно от остальных кнопок
    markup.row(button1, button4)
    markup.row(button5, button3)

    if message.text == '/start':
        # Отправляю приветственный текст
        bot.send_message(message.chat.id, f'Привет, {message.from_user.first_name}!\nУ меня ты сможешь купить некоторые товары!\nКонтакт моего разработчика: https://t.me/z3nkJ', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, 'Перекинул тебя в главном меню! Выбирай!', reply_markup=markup)

# Обработка фото. Если пользователь пришлет фото, то бот отреагирует на него. Можно реализовать свой функционал
@bot.message_handler(content_types='photo')
def get_photo(message):
    bot.send_message(message.chat.id, 'У меня нет возможности просматривать фото :(')

# Обработка обычных текстовых команд, описанных в кнопках
@bot.message_handler()
def info(message):
    if message.text == '🛍 Товары':
        goodsChapter(message)
    elif message.text == '📄 Справка':
        infoChapter(message)
    elif message.text == '🔹 VR sony playstation vr2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)



        bot.send_message(message.chat.id, '👓 Система виртуальной реальности\n\n'
                                          
         'PlayStation VR2 позволяет ощущать эффект полного погружения в любимую игру.\n'
          '💯 Очки обладают общим разрешением 4000x2040 dpi и обзором в 110°. Встроенные датчики помогают'
           'системе точно реагировать на любые движения. Благодаря обработке 3D-звука вы четко ощущаете'
            'все происходящее в игре на 360°.PlayStation VR2 позволяет регулировать расстояние между зрачками'
             'для создания максимального комфорта.\n' '🎦 Система обладает 4 камерами для регистрации движения и ИК-камерой'
              'для отслеживания положения глаз. Шлем дополнен разъемами USB Type-C и jack 3.5 mm. Набор состоит из очков'
              ', набора контроллеров, гарнитуры, кабеля USB и дополнительных аксессуаров.', reply_markup=markup)
    elif message.text == '🔹 HTC VIVE Pro':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '👓 Система виртуальной реальности\n\n'
        '💯 HTC VIVE Pro представляет собой комплект, в который включен шлем, контроллеры и базовые станции SteamVR 2.0.\n'
        'В шлеме предусмотрено 2 экрана, разрешением каждого из которых составляет 1440x1600 пикселей, что позволит вам насладиться невероятно реалистичной картинкой. \n'
         '🎤 Модель HTC VIVE Pro хороша и тем, что в ней появилось 2 микрофона с функцией шумоподавления, обеспечивающих насыщенное и четкое звучание. \n'
        '💻 Система с легкостью подключается к ПК или ноутбуку при помощи USB-интерфейса. \n'
        '👦 Благодаря хорошо продуманной форме шлем подходит к любой форме лица.', reply_markup=markup)
    elif message.text == '🔹 VR Pico 4':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '👓 Система виртуальной реальности \n\n'
                                          '💯 Pico 4 с двумя дисплеями 2.56" выполнен в белом корпусе весом 295 грамм. \n'
                                          ' Модель рассчитана на корпоративное использование. \n'
                                          ' Гарнитура применяется в медицинской, образовательной, игровой сферах, маркетинге, дизайне и VR-разработке. \n'
                                          ' Для подключения в шлеме реализованы технологии Bluetooth иWi-Fi.Pico 4 оборудована дисплеем 4K+ с разрешением 4320x2160. \n'
                                          ' Это позволяет получить четкую и яркую картинку с насыщенными цветами. \n'
                                          '💻 Частота 90 Гц позволяет получить более плавную картинку без резких рывков. \n\n'
                                          '🙌 Благодаря инновационной технологии 6 DoF контроллеры точно отслеживают лицо, глаза и руки. \n'
                                          '💥 Угол обзора 105° расширяет поле зрения пользователя в виртуальном мире. \n'
                                          '💡 Встроенная память 128 ГБ допускает установку игр. Это позволяет не подключать шлем к другим устройствам, \n'
                                          ' а использовать только его.', reply_markup=markup)
    elif message.text == '🔹 VR HP Reverb G2':
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton('💳 Купить')
        button2 = types.KeyboardButton('↩️ Назад')
        markup.row(button1, button2)
        bot.send_message(message.chat.id, '👓 Система виртуальной реальности \n\n'
                                          '💯 HP Reverb G2 состоит из шлема и двух контроллеров, адаптера питания и кабеля подключения. \n'
                                          ' Благодаря наушникам и набору встроенных датчиков вы ощутите полное погружение и непередаваемые эмоции. \n'
                                          '💻 Устройство совместимо с PC, ПК или ноутбуком с указанными в документации к модели требованиями. \n'
                                          ' Шлем HP Reverb G2 обеспечивает разрешение дисплеев каждого глаза 2160x2160 dpi, а действует с частотой обновления 90 Гц. \n'
                                          '🎦 Устройство оснащено четырьмя камерами для регистрации всех движений, дополнено акселерометром, магнитометром и гироскопом.', reply_markup=markup)
    elif message.text == '⭐ Отзывы':
        # Функционал не придумал
        bot.send_message(message.chat.id, '⭐⭐⭐⭐⭐ \n\n'' Сайт классный, заказал себе шикарные VR-очки, очень счастлив приобретению')
        bot.send_message(message.chat.id,'⭐⭐⭐⭐⭐ \n\n'' Люблю смотреть их ролики на Ютубе и мечтать о новеньких моделях гарнитуры для моих очков')
        bot.send_message(message.chat.id,
                         '⭐⭐⭐⭐⭐ \n\n'' Подписан на их Телеграмм, узнал там очень много классного о VR индустрии')
        bot.send_message(message.chat.id,
                         '⭐⭐⭐⭐⭐ \n\n'' Использовал телеграмм-бот, чтобы заказать себе крутые очки. Всё очень понравилось, рекомендую')
        bot.send_message(message.chat.id,
                         '⭐⭐⭐⭐⭐ \n\n'' Краем уха что-то слышал о VR технологиях, но этот сайт помог мне узнать много нового. Теперь очень сильно хочу накопить денег и купить новенькие VR-очки')
    elif message.text == '💳 Купить' or message.text == '✏️ Написать разработчику':
        # Сюда можете ввести свою ссылку на Телеграмм, тогда пользователя будет перекидывать к вам в личку
        webbrowser.open('https://t.me/z3nkJ')
    elif message.text == '↩️ Назад':
        goodsChapter(message)
    elif message.text == '↩️ Назад в меню':
        welcome(message)
    elif message.text == '⁉ FAQ':
        bot.send_message(message.chat.id, '✅ Что мне это даст? \n'
                                                'Вы получите доступ к эксклюзивным инструментам и функциям, которые помогут вам улучшить вашу стратегию торговли и увеличить ваш доход. Мы постоянно обновляем наше приложение, чтобы вы всегда были в курсе последних новостей и тенденций на рынке криптовалют. \n\n'
                                                '✅ Сколько продлится подписка? \n'
                                                'Длительность подписки - это ваш выбор! Мы предлагаем различные варианты подписки, от коротких до долгосрочных, чтобы каждый мог выбрать оптимальный вариант для себя. \n\n'
                                                '✅ Как совершать честный обмен? \n'
                                                'Наше приложение предоставляет вам доступ к надежным и проверенным криптобиржам, где вы можете совершать торговлю безопасно. Мы также предоставляем обзоры бирж и рекомендации по выбору наиболее надежных площадок для торговли. \n\n'
                                                '✅ Как мне выводить прибыль? \n'
                                                'Наше приложение предоставляет удобные инструменты для вывода прибыли. Вы можете выбирать различные способы вывода средств, включая банковские переводы, электронные кошельки и другие платежные системы. \n\n'
                                                '✅ Как вернуть деньги за подписку? \n'
                                                'Мы предоставляем возможность вернуть деньги за подписку в течение двух недель после ее оформления. Если вы обнаружите, что наше приложение не соответствует вашим ожиданиям, мы вернем вам деньги без лишних вопросов.')

    # Если пользователь написал свое сообщение, то бот рандомно генерирует один из возможных вариантов ответа
    # Добавлять и редактировать варианты ответов можно в списке answers
    else:
        bot.send_message(message.chat.id, answers[random.randint(0, 3)])



# Функция, отвечающая за раздел товаров
def goodsChapter(message):
    # Кнопки для товаров
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('🔹 VR sony playstation vr2')
    button2 = types.KeyboardButton('🔹 HTC VIVE Pro')
    button3 = types.KeyboardButton('🔹 VR Pico 4')
    button4 = types.KeyboardButton('🔹 VR HP Reverb G2')
    button5 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    markup.row(button3, button4)
    markup.row(button5)

    # Отправляем сообщение с прикрепленными к нему кнопками товаров
    bot.send_message(message.chat.id, 'Вот все товары, которые сейчас находятся в продаже:', reply_markup=markup)

# Функция, отвечающая за раздел настроек
# def settingsChapter(message):
#     markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     button1 = types.KeyboardButton('⚙️ Настройки #1')
#     button2 = types.KeyboardButton('⚙️ Настройки #2')
#     button3 = types.KeyboardButton('↩️ Назад в меню')
#     markup.row(button1, button2)
#     markup.row(button3)
#     bot.send_message(message.chat.id, 'Раздел настроек.\nВыбери один из вариантов:', reply_markup=markup)

# Функция, отвечающая за раздел помощи
def infoChapter(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton('✏️ Написать разработчику')
    button2 = types.KeyboardButton('↩️ Назад в меню')
    markup.row(button1, button2)
    bot.send_message(message.chat.id, 'Раздел справки.\n✔ История магазина VR очков началась в далеком 2015 году, когда технологии виртуальной реальности только начали набирать популярность. \n\n'
                                            '💲 Магазин также активно участвовал в благотворительных акциях, направленных на поддержку детей и взрослых с ограниченными возможностями, например, акция "VR для всех". \n\n'
                                            '💹 В рамках ежегодных фестивалей проходили мастер-классы, лекции от экспертов в области виртуальной реальности, а также демонстрации новейших разработок в этой области', reply_markup=markup)

# Строчка, чтобы программа не останавливалась
bot.polling(none_stop=True)


























