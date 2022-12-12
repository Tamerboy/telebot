import telebot
from telebot import types
import openpyxl

token = "5455203432:AAGtoVZUtaCbr10XUKZXlsSMPstoOj3h64E"
bot = telebot.TeleBot(token)

@bot.message_handler(commands=["getdata"])
def getdata(message):
    bot.send_document(message.from_user.id, open(r'data.xlsx', 'rb'))

@bot.message_handler(commands=["start"])
def start(message):
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Қазақша")
    but2 = types.KeyboardButton("Русский")
    menu.add(but1)
    menu.add(but2)
    bot.send_message(message.chat.id, "Қош келдіңіз! | Добро пожаловать! \n Тілді таңдаңыз: | Выберите язык:", reply_markup=menu)
    bot.register_next_step_handler(message, age)

@bot.message_handler(func=lambda message:True)
def age(message):
    if message.text == "Русский":
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("18-24")
        but2 = types.KeyboardButton("25-39")
        but3 = types.KeyboardButton("40-54")
        but4 = types.KeyboardButton("55-69")
        but5 = types.KeyboardButton("70-84")
        but6 = types.KeyboardButton("85 и более")
        menu.add(but1)
        menu.add(but2)
        menu.add(but3)
        menu.add(but4)
        menu.add(but5)
        menu.add(but6)
        bot.send_message(message.from_user.id,"Ваш возраст:", reply_markup=menu)
        bot.register_next_step_handler(message,gender)
    elif message.text == "Қазақша":
        menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        but1 = types.KeyboardButton("18-24")
        but2 = types.KeyboardButton("25-39")
        but3 = types.KeyboardButton("40-54")
        but4 = types.KeyboardButton("55-69")
        but5 = types.KeyboardButton("70-84")
        but6 = types.KeyboardButton("85 және жоғары")
        menu.add(but1)
        menu.add(but2)
        menu.add(but3)
        menu.add(but4)
        menu.add(but5)
        menu.add(but6)
        bot.send_message(message.from_user.id,"Сіздің жасыңыз:", reply_markup=menu)
        bot.register_next_step_handler(message, kazgender)

@bot.message_handler(func=lambda message:True)
def gender(message):
    agevar = message.text
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Мужской")
    but2 = types.KeyboardButton("Женский")
    menu.add(but1)
    menu.add(but2)
    bot.send_message(message.from_user.id, "Ваш пол:", reply_markup=menu)
    bot.register_next_step_handler(message, categories, agevar)




@bot.message_handler(func=lambda message:True)
def kazgender(message):
    agevar = message.text
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Ер")
    but2 = types.KeyboardButton("Әйел")
    menu.add(but1)
    menu.add(but2)
    bot.send_message(message.from_user.id, "Сіздің жынысыңыз:", reply_markup=menu)
    bot.register_next_step_handler(message, kazcategories,agevar)

@bot.message_handler(func=lambda message:True)
def categories(message,agevar):
    gendervar = message.text
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Да")
    but2 = types.KeyboardButton("Нет")
    menu.add(but1)
    menu.add(but2)
    bot.send_message(message.from_user.id,"Входите ли вы в льготную категорию?", reply_markup=menu)
    bot.register_next_step_handler(message,categorieshandler, agevar, gendervar)


@bot.message_handler(func=lambda message: True)
def kazcategories(message,agevar):
    gendervar = message.text
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but1 = types.KeyboardButton("Иә")
    but2 = types.KeyboardButton("Жоқ")
    menu.add(but1)
    menu.add(but2)
    bot.send_message(message.from_user.id, "Сіз жеңілдік санатына кіресіз бе?", reply_markup=menu)
    bot.register_next_step_handler(message,categorieshandler, agevar, gendervar)

@bot.message_handler(func=lambda message:True)
def categorieshandler(message, agevar, gendervar):
    rusmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    but = types.KeyboardButton("Продолжить")
    rusmenu.add(but)

    kazmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kazbut = types.KeyboardButton("Жалғастыру")
    kazmenu.add(kazbut)

    ruslist = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lbut1 = types.KeyboardButton("Дети до 18 лет")
    lbut2 = types.KeyboardButton("Беременные женщины")
    lbut3 = types.KeyboardButton("Пенсионеры по возрасту")
    lbut4 = types.KeyboardButton("Участники ВОВ")
    lbut5 = types.KeyboardButton("Инвалиды I, II, III группы")
    lbut6 = types.KeyboardButton("Многодетные матери, обладатели «Алтын алка» и «Кумыс алка»")
    lbut7 = types.KeyboardButton("Получатели адресной социальной помощи")
    lbut8 = types.KeyboardButton("Больные инфекционными и социально значимыми заболеваниями")
    lbut9 = types.KeyboardButton("Неработающие казастанцы, ухаживающие за ребенком инвалидом")
    ruslist.add(lbut1)
    ruslist.add(lbut2)
    ruslist.add(lbut3)
    ruslist.add(lbut4)
    ruslist.add(lbut5)
    ruslist.add(lbut6)
    ruslist.add(lbut7)
    ruslist.add(lbut8)
    ruslist.add(lbut9)
    kazlist = types.ReplyKeyboardMarkup(resize_keyboard=True)
    klbut1 = types.KeyboardButton("18 жасқа дейінгі балалар")
    klbut2 = types.KeyboardButton("Жүкті әйелдер")
    klbut3 = types.KeyboardButton("Жасы бойынша зейнеткерлер")
    klbut4 = types.KeyboardButton("ҰОС қатысушылары")
    klbut5 = types.KeyboardButton("I, II, III топтағы мүгедектер")
    klbut6 = types.KeyboardButton("«Алтын алқа» және «Күміс алқа» иегерлері")
    klbut7 = types.KeyboardButton("Атаулы әлеуметтік көмек алушылар")
    klbut8 = types.KeyboardButton("Жұқпалы және әлеуметтік маңызы бар аурулармен ауыратын науқастар")
    klbut9 = types.KeyboardButton("Ерекше қажеттіліктері бар, мүгедек балаларға күтім жасайтын жұмыс істемейтін қазақстандықтар.")
    kazlist.add(klbut1)
    kazlist.add(klbut2)
    kazlist.add(klbut3)
    kazlist.add(klbut4)
    kazlist.add(klbut5)
    kazlist.add(klbut6)
    kazlist.add(klbut7)
    kazlist.add(klbut8)
    kazlist.add(klbut9)

    if message.text == "Нет":
        bot.send_message(message.from_user.id, "Направить в меню",reply_markup=rusmenu)
        bot.register_next_step_handler(message,ruslanguage1,agevar,gendervar)
    elif message.text == "Жоқ":
        bot.send_message(message.from_user.id, "Негізгі бөлімге жалғастыру",reply_markup=kazmenu)
        bot.register_next_step_handler(message,kazlanguage1, agevar,gendervar)
    elif message.text == "Да":
        bot.send_message(message.from_user.id, "Выберите категорию:",reply_markup=ruslist)
        bot.register_next_step_handler(message, ruslanguage1,agevar,gendervar)
    elif message.text == "Иә":
        bot.send_message(message.from_user.id, "Өзіңіздің санатыңызды таңдаңыз:",reply_markup=kazlist)
        bot.register_next_step_handler(message, kazlanguage1,agevar,gendervar)

@bot.message_handler(func=lambda message:True)
def ruslanguage1(message,agevar,gendervar):
    result = message.text
    dan = []
    dan.append(result)
    dan.append(agevar)
    dan.append(gendervar)
    wb = openpyxl.load_workbook('data.xlsx')
    sheet = wb['Лист1']
    sheet.append(dan)
    wb.save('data.xlsx')
    but1 = types.KeyboardButton("Получить информацию об экстренной стоматологической помощи")
    but2 = types.KeyboardButton("Получить информацию о плановой стоматологической помощи")
    but3 = types.KeyboardButton("Получить информацию о клиниках оказывающих бесплатную стоматологическую помощь")
    but4 = types.KeyboardButton("Получить информацию о бесплатной ортодонтической помощи")
    but5 = types.KeyboardButton("Дополнительная информация")
    but6 = types.KeyboardButton("⬅Выход")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but1)
    menu.add(but2)
    menu.add(but3)
    menu.add(but4)
    menu.add(but5)
    menu.add(but6)
    bot.send_message(message.from_user.id,
                     "Для продолжения выберите раздел:",
                     reply_markup=menu)
    bot.register_next_step_handler(message, rusmenuhandler)

@bot.message_handler(func=lambda message:True)
def ruslanguage(message):
    but1 = types.KeyboardButton("Получить информацию об экстренной стоматологической помощи")
    but2 = types.KeyboardButton("Получить информацию о плановой стоматологической помощи")
    but3 = types.KeyboardButton("Получить информацию о клиниках оказывающих бесплатную стоматологическую помощь")
    but4 = types.KeyboardButton("Получить информацию о бесплатной ортодонтической помощи")
    but5 = types.KeyboardButton("Дополнительная информация")
    but6 = types.KeyboardButton("⬅Выход")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but1)
    menu.add(but2)
    menu.add(but3)
    menu.add(but4)
    menu.add(but5)
    menu.add(but6)
    bot.send_message(message.from_user.id,
                     "Для продолжения выберите раздел:",
                     reply_markup=menu)
    bot.register_next_step_handler(message, rusmenuhandler)

@bot.message_handler(func=lambda message:True)
def kazlanguage1(message,agevar, gendervar):
    result = message.text
    dan = []
    dan.append(result)
    dan.append(agevar)
    dan.append(gendervar)
    wb = openpyxl.load_workbook('data.xlsx')
    sheet = wb['Лист1']
    sheet.append(dan)
    wb.save('data.xlsx')
    kazbut1 = types.KeyboardButton("Шұғыл стоматологиялық көмек жайлы ақпарат алу")
    kazbut2 = types.KeyboardButton("Жоспарлы стоматологиялық көмек жайлы ақпарат алу")
    kazbut3 = types.KeyboardButton("Тегін стоматологиялық көмек көрсететін клиникалар жайлы ақпарат алу")
    kazbut4 = types.KeyboardButton("Тегін ортодонтиялық көмек жайлы ақпарат алу")
    kazbut5 = types.KeyboardButton("Қосымша ақпарат")
    kazbut6 = types.KeyboardButton("Шығу")
    kazmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kazmenu.add(kazbut1)
    kazmenu.add(kazbut2)
    kazmenu.add(kazbut3)
    kazmenu.add(kazbut4)
    kazmenu.add(kazbut5)
    kazmenu.add(kazbut6)
    bot.send_message(message.from_user.id,
                     "Қайырлы күн! Бұл Қзақстан Республикасында тегін стоматологиялық көмек жайлы ақпарат алуға арналған бот.\n Жалғастыру үшін келесі бөлімдердің бірін таңдаңыз: ",
                     reply_markup=kazmenu)
    bot.register_next_step_handler(message, kazmenuhandler)

@bot.message_handler(func=lambda message:True)
def kazlanguage(message):
    kazbut1 = types.KeyboardButton("Шұғыл стоматологиялық көмек жайлы ақпарат алу")
    kazbut2 = types.KeyboardButton("Жоспарлы стоматологиялық көмек жайлы ақпарат алу")
    kazbut3 = types.KeyboardButton("Тегін стоматологиялық көмек көрсететін клиникалар жайлы ақпарат алу")
    kazbut4 = types.KeyboardButton("Тегін ортодонтиялық көмек жайлы ақпарат алу")
    kazbut5 = types.KeyboardButton("Қосымша ақпарат")
    kazbut6 = types.KeyboardButton("Шығу")
    kazmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    kazmenu.add(kazbut1)
    kazmenu.add(kazbut2)
    kazmenu.add(kazbut3)
    kazmenu.add(kazbut4)
    kazmenu.add(kazbut5)
    kazmenu.add(kazbut6)
    bot.send_message(message.from_user.id,
                     "Қайырлы күн! Бұл Қзақстан Республикасында тегін стоматологиялық көмек жайлы ақпарат алуға арналған бот.\n Жалғастыру үшін келесі бөлімдердің бірін таңдаңыз: ",
                     reply_markup=kazmenu)
    bot.register_next_step_handler(message, kazmenuhandler)

@bot.message_handler(func=lambda message:True)
def rusmenuhandler(message):
    lbut = types.KeyboardButton("Да")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    backbut = types.KeyboardButton("Назад")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(backbut)
    if message.text == "Получить информацию об экстренной стоматологической помощи":
        abut = types.KeyboardButton("Какие случаи считаются неотложными")
        abut1 = types.KeyboardButton("Кто может получить экстренную стоматологическую помощь")
        abut2 = types.KeyboardButton("Какие слуги входят в экстренную стоматологическую помощь")
        abut3 = types.KeyboardButton("Каковы предельные сроки ожидания экстренной стоматологической помощи")
        abut4 = types.KeyboardButton("⬅Назад")
        menu1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu1.add(abut)
        menu1.add(abut1)
        menu1.add(abut2)
        menu1.add(abut3)
        menu1.add(abut4)
        bot.send_message(message.from_user.id, "Выберите подраздел", reply_markup=menu1)
        bot.register_next_step_handler(message, butinfohandler)
    elif message.text == "Получить информацию о плановой стоматологической помощи":
        bbut = types.KeyboardButton("Кто может получить плановую стоматологическую помощь")
        bbut1 = types.KeyboardButton("Какие услуги входят в плановую стоматологическую помощь")
        bbut2 = types.KeyboardButton("Имеется ли лимит на получение плановой бесплатной стоматологической помощи")
        bbut3 = types.KeyboardButton("Как записаться на прием")
        bbut4 = types.KeyboardButton("⬅Назад")
        bmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bmenu.add(bbut)
        bmenu.add(bbut1)
        bmenu.add(bbut2)
        bmenu.add(bbut3)
        bmenu.add(bbut4)
        bot.send_message(message.from_user.id, "Выберите подраздел", reply_markup=bmenu)
        bot.register_next_step_handler(message, butinfohandler1)

    elif message.text == "Получить информацию о клиниках оказывающих бесплатную стоматологическую помощь":
        zbut = types.KeyboardButton("Получить бесплатную стоматологическую помощь в частных клиниках")
        zbut1 = types.KeyboardButton("Список клиник оказывающие бесплатную стоматологическую помощь")
        zbut2 = types.KeyboardButton("Нужно ли направление специалиста")
        zbut3 = types.KeyboardButton("Как записаться на прием")
        zbut4 = types.KeyboardButton("Какие документы нужно иметь при себе")
        zbut5 = types.KeyboardButton("Имеется ли лимит на получение бесплатной стоматологической помощи")
        zbut6 = types.KeyboardButton("⬅Назад")
        zmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        zmenu.add(zbut)
        zmenu.add(zbut1)
        zmenu.add(zbut2)
        zmenu.add(zbut3)
        zmenu.add(zbut4)
        zmenu.add(zbut5)
        zmenu.add(zbut6)
        bot.send_message(message.from_user.id, "Выберите подраздел", reply_markup=zmenu)
        bot.register_next_step_handler(message, butinfohandler2)

    elif message.text == "Получить информацию о бесплатной ортодонтической помощи":
        bot.send_message(message.from_user.id, "Бесплатную ортодонтическую помощь оказывают:\n- детям с врождённо челюстно-лицевой патологией (расщелины верхней губы и нёба);\n- детям из малообеспеченных семей с 6 до 12 лет с различными видами зубочелюстных аномалий (дефекты прикуса и микрогнатия челюсти)", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)

    elif message.text == "Дополнительная информация":
        bot.send_message(message.from_user.id, "Всю подробную информацию можете получить на официальном сайте fms.kz, через мобильное приложение Qoldau 24/7 и контакт-центр по номеру 1406.")
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)

    elif message.text == "⬅Выход":
        lbut = types.KeyboardButton("Да")
        lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        lmenu.add(lbut)
        bot.send_message(message.from_user.id, "Вернуться к выбору языка?", reply_markup=lmenu)
        bot.register_next_step_handler(message,start)

@bot.message_handler(func=lambda message:True)
def kazmenuhandler(message):
    lbut = types.KeyboardButton("Иә")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    backbut = types.KeyboardButton("Шығу")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(backbut)
    if message.text == "Шұғыл стоматологиялық көмек жайлы ақпарат алу":
        abut = types.KeyboardButton("Қандай жағдайлар шұғыл болып саналады")
        abut1 = types.KeyboardButton("Қай санаттағы азаматтар шұғыл стоматологиялық көмекке жүгіне алады")
        abut2 = types.KeyboardButton("Шұғыл стоматологиялық көмек қатарына қандай көмек тегін қарастырылған")
        abut3 = types.KeyboardButton("Шұғыл стоматологиялық көмекті алу кезектілігі қандай")
        abut4 = types.KeyboardButton("Шығу")
        menu1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
        menu1.add(abut)
        menu1.add(abut1)
        menu1.add(abut2)
        menu1.add(abut3)
        menu1.add(abut4)
        bot.send_message(message.from_user.id, "Бөлікшелердің бірін таңдаңыз", reply_markup=menu1)
        bot.register_next_step_handler(message, kazbutinfohandler)
    elif message.text == "Жоспарлы стоматологиялық көмек жайлы ақпарат алу":
        bbut = types.KeyboardButton("Қай санаттағы азаматтар жоспарлы стоматологиялық көмекке жүгіне алады")
        bbut1 = types.KeyboardButton("Жоспарлы стоматологиялық көмек қатарына қандай көмек тегін қарастырылған")
        bbut2 = types.KeyboardButton("Жоспарлы стоматологиялық ем алуға лимит бар ма?")
        bbut3 = types.KeyboardButton("Қабылдауға қалай жазылуға болады")
        bbut4 = types.KeyboardButton("Шығу")
        bmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bmenu.add(bbut)
        bmenu.add(bbut1)
        bmenu.add(bbut2)
        bmenu.add(bbut3)
        bmenu.add(bbut4)
        bot.send_message(message.from_user.id, "Бөлікшелердің бірін таңдаңыз", reply_markup=bmenu)
        bot.register_next_step_handler(message, kazbutinfohandler1)

    elif message.text == "Тегін стоматологиялық көмек көрсететін клиникалар жайлы ақпарат алу":
        zbut = types.KeyboardButton("Жеке клиникалардан тегін стоматологиялық көмек алу")
        zbut1 = types.KeyboardButton("Тегін стоматологиялық көмек көрсететін жеке клиникалар тізімі")
        zbut2 = types.KeyboardButton("Учаскелік дәрігердің жолдамасы талап етіледі ме")
        zbut3 = types.KeyboardButton("Қабылдауға қалай жазылуға болады")
        zbut4 = types.KeyboardButton("Қандай құжаттар қажет")
        zbut5 = types.KeyboardButton("Тегін стоматологиялық ем алуға лимит бар ма")
        zbut6 = types.KeyboardButton("Шығу")
        zmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        zmenu.add(zbut)
        zmenu.add(zbut1)
        zmenu.add(zbut2)
        zmenu.add(zbut3)
        zmenu.add(zbut4)
        zmenu.add(zbut5)
        zmenu.add(zbut6)
        bot.send_message(message.from_user.id, "Бөлікшелердің бірін таңдаңыз", reply_markup=zmenu)
        bot.register_next_step_handler(message, kazbutinfohandler2)

    elif message.text == "Тегін ортодонтиялық көмек жайлы ақпарат алу":
        bot.send_message(message.from_user.id, "6 жастан 12 жасқа дейінгі балаларға түрлі жақсүйек-бет аймағының ауытқулары (тістем бұзылулары, жақтың микрогнотиясы) кезінде ортодонтиялық көмек көрсетіледі.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)

    elif message.text == "Қосымша ақпарат":
        bot.send_message(message.from_user.id, "Егер сізде стоматологиялық көмек алуға қатысты сұрақтар туындаған болса, сіз әрбір медицина ұйымында бар Пациенттерді қолдау қызметіне, fms.kz ресми сайтына, 1406 байланыс орталығына, Qoldau 24/7 мобильді қосымшасына  жүгіне аласыз.")
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)

    elif message.text == "Шығу":
        lbut = types.KeyboardButton("Иә")
        lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
        lmenu.add(lbut)
        bot.send_message(message.from_user.id, "Тілді таңдауға оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message,start)

@bot.message_handler(func=lambda message:True)
def butinfohandler(message):
    lbut = types.KeyboardButton("Да")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    but = types.KeyboardButton("Назад")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but)
    if message.text == "Какие случаи считаются неотложными":
        bot.send_message(message.from_user.id, "Неотложными считаются(острая боль):\n- пульпит (острый иои обострение хронического);\n- периодонтит (острый и обострение хронического);\n- челюстно-лицевая травма (вывих или перелом зуба);\n- обострении одонтогенных и недонтогенных воспалительных заболеваний челюстно-лицевой области;\n- стоматит;\n- острые болезненные состояния, лечение которых требует оперативного вмешательства.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Кто может получить экстренную стоматологическую помощь":
        bot.send_message(message.from_user.id, "Экстренную помощь могут получить:\n- дети до 18 лет, беременные женщины;\n- участники ВОВ и приравненные к ним лица;\n- инвалиды I, II, III групп;\n- многодетные матери, награждённые подвесками \"Алтын алка\" и \"Кумыс алка\";\n- получатели адресной социальной помощи;\n- пенсионеры по возрасту;\n- больные инфекционными и социально значимыми заболеваниями и заболеваниями, представляющими опасность для окружающих;\n- неработающие казахстанцы, ухаживающие за ребёнком с особыми потребностями или инвалидом I группы с детства.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Какие слуги входят в экстренную стоматологическую помощь":
        bot.send_message(message.from_user.id, "Экстренная стоматологическая помощь включает в себя: анестезию, рентгенографию челюсти или зуба, удаление зуба, препарирование и наложение пломбы, лечение пульпита, периодонтита, острых форм стоматита, альвеолита, вскрытие абсцесса.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Каковы предельные сроки ожидания экстренной стоматологической помощи":
        bot.send_message(message.from_user.id, "В экстренной медицинской помощи нет очередности, обратитесь за помощью в государственную поликлинику или в любую стоматологическую клинику, которая является поставщиком ФМС.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "⬅Назад":
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)

@bot.message_handler(func=lambda message:True)
def kazbutinfohandler(message):
    lbut = types.KeyboardButton("Иә")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    but = types.KeyboardButton("Шығу")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but)
    if message.text == "Қандай жағдайлар шұғыл болып саналады":
        bot.send_message(message.from_user.id, "Пульпит (өткір немесе созылмалы); \nпериодонтит (өткір және созылмалы); \nжақ-бет жарақаты (мысалы, тістің таюы немесе сынуы); \nжақ-бет аймағының одонтогендік және одонтогендік емес қабыну ауруларының өршу белгілері; \nстоматит; \nөткір ауыру жағдайларында; \nжедел араласуды қажет ететін емдеу әдісі.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Қай санаттағы азаматтар шұғыл стоматологиялық көмекке жүгіне алады":
        bot.send_message(message.from_user.id, "Зейнеткерлер, көп балалы аналар, мүгедектер, оларға күтім жасайтын жұмыссыздар, АӘК алушылар, сондай-ақ белгілі бір аурулармен есепте тұрған пациенттер де тегін стоматологиялық көмек ала алады.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Шұғыл стоматологиялық көмек қатарына қандай көмек тегін қарастырылған":
        bot.send_message(message.from_user.id, "Анестезия; \nжақ немесе тістің рентгенографиясы; \nтісті жұлу; \nпериостотомия; \nпульпит, периодонтит, стоматиттің жедел түрлерін, альвеолитті емдеу; абсцессті ашу.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Шұғыл стоматологиялық көмекті алу кезектілігі қандай":
        bot.send_message(message.from_user.id, "Шұғыл стоматологиялық көмекте кезектілік жоқ, көмекті алу үшін жергілікті емханаға немесе клиникаға жедел жүгіне аласыз. Бұл ретте, стоматологиялық қызмет көрсететін клиника сақтандыру қорының әлеуетті жеткізушісі және әлеуетті жеткізушісі тізімінде болуы тиіс.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Шығу":
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)



@bot.message_handler(func=lambda message:True)
def butinfohandler1(message):
    lbut = types.KeyboardButton("Да")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    but = types.KeyboardButton("Назад")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but)
    if message.text == "Кто может получить плановую стоматологическую помощь":
        bot.send_message(message.from_user.id, "Плановая стоматологическая помощь предусмотрена пакетом ОСМС для детей до 18 лет и беременных женщин.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Какие услуги входят в плановую стоматологическую помощь":
        bot.send_message(message.from_user.id, "В плановую стоматологическую помощь входит:\n- рентгенография челюсти или зуба; \n- анестезия; \n- препарирование и наложение пломбы;\n- удаление зубов с использованием обезболивания (по направлению специалиста).", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Имеется ли лимит на получение плановой бесплатной стоматологической помощи":
        bot.send_message(message.from_user.id, "Лимита на объемы и количество посещений нет.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Как записаться на прием":
        bot.send_message(message.from_user.id, "Для получения услуг можно выбрать частную стоматологию, которая имеет договор с Фондом медицинского страхования, либо обратиться в стоматологический кабинет своей поликлиники.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "⬅Назад":
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)

@bot.message_handler(func=lambda message:True)
def kazbutinfohandler1(message):
    lbut = types.KeyboardButton("Иә")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    but = types.KeyboardButton("Шығу")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but)
    if message.text == "Қай санаттағы азаматтар жоспарлы стоматологиялық көмекке жүгіне алады":
        bot.send_message(message.from_user.id, "Балалар мен жүкті әйелдер жоспарлы стоматологиялық көмекті тегін алады", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Жоспарлы стоматологиялық көмек қатарына қандай көмек тегін қарастырылған":
        bot.send_message(message.from_user.id, "Анестезия; \nжақ немесе тістің рентгенографиясы; тісті жұлу; \nдайындау және пломба салу; периостотомия; \nпульпит, периодонтит, стоматиттің жедел түрлерін, альвеолитті емдеу; абсцессті ашу.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Жоспарлы стоматологиялық ем алуға лимит бар ма":
        bot.send_message(message.from_user.id, "Жоспарлы стоматологиялық ем алуға лимит жоқ", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Қабылдауға қалай жазылуға болады":
        bot.send_message(message.from_user.id, "Қормен келісімшарты бар жеке стоматологиялық клиникаға телфон арқылы немесе жеке барып қабылдауға жазылу немесе өз емханаңыздың стоматологиялық кабинетіне жүгінуге болады.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Шығу":
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)

@bot.message_handler(func=lambda message: True)
def kazbutinfohandler2(message):
    lbut = types.KeyboardButton("Иә")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    but = types.KeyboardButton("Шығу")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but)
    rbut = types.KeyboardButton("Иә")
    rmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rmenu.add(rbut)
    if message.text == "Жеке клиникалардан тегін стоматологиялық көмек алу":
        bot.send_message(message.from_user.id, "Жеке стоматологиялық клиникаға жүгіне аласыз. Бұл ретте, стоматологиялық қызмет көрсететін клиника сақтандыру қорының әлеуетті жеткізушісі болуы тиіс және әлеуетті жеткізушісі тізімінде болуы міндетті.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "":
        bot.send_message(message.from_user.id,"Қала немесе облысын таңдауға жалғастыру?",reply_markup=rmenu)
        bot.register_next_step_handler(message,kazcliniclist)

    elif message.text == "Тегін стоматологиялық көмек көрсететін жеке клиникалар тізімі":
        bot.send_message(message.from_user.id, "", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Учаскелік дәрігердің жолдамасы талап етіледі ме":
        bot.send_message(message.from_user.id, "Шұғыл және жоспарлы стоматологиялық көмек көрсету пациенттің еркін таңдауы негізінде жүзеге асырылады және пациенттің тіркелген жері бойынша учаскелік дәрігердің жолдамасының болуы талап етілмейді.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Қабылдауға қалай жазылуға болады":
        bot.send_message(message.from_user.id, "Қормен келісімшарты бар жеке стоматологиялық клиникаға телфон арқылы немесе жеке барып қабылдауға жазылу немесе өз емханаңыздың стоматологиялық кабинетіне жүгінуге болады.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Қандай құжаттар қажет":
        bot.send_message(message.from_user.id, "Жеке куәлік; \n18 жасқа толмаған балалар үшін туу туралы куәлік (ата-ана немесе заңды өкілімен бірге);\nӘлеуметтік жеңілдік санатын растайтын құжат; ", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Қабылдауға қалай жазылуға болады":
        bot.send_message(message.from_user.id, "Қормен келісімшарты бар жеке стоматологиялық клиникаға телфон арқылы немесе жеке барып қабылдауға жазылу немесе өз емханаңыздың стоматологиялық кабинетіне жүгінуге болады.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)
    elif message.text == "Шығу":
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?",reply_markup=lmenu)
        bot.register_next_step_handler(message,kazlanguage)

@bot.message_handler(func=lambda message: True)
def butinfohandler2(message):
    lbut = types.KeyboardButton("Да")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    but = types.KeyboardButton("Назад")
    menu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu.add(but)
    rbut = types.KeyboardButton("Да")
    rmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    rmenu.add(rbut)
    if message.text == "Получить бесплатную стоматологическую помощь в частных клиниках":
        bot.send_message(message.from_user.id, "Да, можно выбрать частную стоматологию, которая имеет договор с Фондом медицинского страхования.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Список клиник оказывающие бесплатную стоматологическую помощь":
        bot.send_message(message.from_user.id,"Выбрать область или город из списка?",reply_markup=rmenu)
        bot.register_next_step_handler(message,cliniclist)

    elif message.text == "Нужно ли направление специалиста":
        bot.send_message(message.from_user.id, "Оказание стоматологической помощи осуществляется на основе свободного выбора пациентом медицинской организации, направление участкового врача не требуется.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Как записаться на прием":
        bot.send_message(message.from_user.id, "Для записи обратитесь или позвоните в выбранную вами клинику.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "Какие документы нужно иметь при себе":
        bot.send_message(message.from_user.id, "- Удостоверение личности.;\n- для детей до 18 лет свидетельство о рождении (сопровождение родителя или законного представителя);\n- документы подтверждающие льготную категорию.", reply_markup=menu)
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)
    elif message.text == "⬅Назад":
        bot.send_message(message.from_user.id, "Вернуться в главное меню?",reply_markup=lmenu)
        bot.register_next_step_handler(message,ruslanguage)


@bot.message_handler(func=lambda message:True)
def cliniclist(message):
    but = types.KeyboardButton("Акмолинская область")
    but1 = types.KeyboardButton("Актюбинская область")
    but2 = types.KeyboardButton("Алматинская область")
    but3 = types.KeyboardButton("Атырауская область")
    but4 = types.KeyboardButton("Восточно-Казахстанская область")
    but5 = types.KeyboardButton("г.Алматы")
    but6 = types.KeyboardButton("г.Астана")
    but7 = types.KeyboardButton("г.Шымкент")
    but8 = types.KeyboardButton("Жамбылская область")
    but9 = types.KeyboardButton("Западно-Казахстанская область")
    but10 = types.KeyboardButton("Карагандинская область")
    but11 = types.KeyboardButton("Костанайская область")
    but12 = types.KeyboardButton("Кызылординская область")
    but13 = types.KeyboardButton("Мангистауская область")
    but14 = types.KeyboardButton("Павлодарская область")
    but15 = types.KeyboardButton("Северо-Казахстанская область")
    but16 = types.KeyboardButton("Туркестанская область")
    but17 = types.KeyboardButton("Назад")
    regions = types.ReplyKeyboardMarkup(resize_keyboard=True)
    regions.add(but)
    regions.add(but1)
    regions.add(but2)
    regions.add(but3)
    regions.add(but4)
    regions.add(but5)
    regions.add(but6)
    regions.add(but7)
    regions.add(but8)
    regions.add(but9)
    regions.add(but10)
    regions.add(but11)
    regions.add(but12)
    regions.add(but13)
    regions.add(but14)
    regions.add(but15)
    regions.add(but16)
    regions.add(but17)
    bot.send_message(message.from_user.id, "Выберите область/город", reply_markup=regions)
    bot.register_next_step_handler(message, cliniclisthandler)

@bot.message_handler(func=lambda message:True)
def cliniclisthandler(message):
    lbut = types.KeyboardButton("Да")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    if message.text == "Акмолинская область":
        bot.send_document(message.from_user.id, open(r'Акмолинская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Актюбинская область":
        bot.send_document(message.from_user.id, open(r'Актюбинская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Алматинская область":
        bot.send_document(message.from_user.id, open(r'Алматинская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Атырауская область":
        bot.send_document(message.from_user.id, open(r'Атырауская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Восточно-Казахстанская область":
        bot.send_document(message.from_user.id, open(r'Восточно-Казахстанская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "г.Алматы":
        bot.send_document(message.from_user.id, open(r'г. Алматы.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "г.Астана":
        bot.send_document(message.from_user.id, open(r'г. Астана.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "г.Шымкент":
        bot.send_document(message.from_user.id, open(r'г. Шымкент.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Жамбылская область":
        bot.send_document(message.from_user.id, open(r'Жамбылская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Западно-Казахстанская область":
        bot.send_document(message.from_user.id, open(r'Западно-Казахстанская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Карагандинская область":
        bot.send_document(message.from_user.id, open(r'Карагандинская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Костанайская область":
        bot.send_document(message.from_user.id, open(r'Костанайская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Кызылординская область":
        bot.send_document(message.from_user.id, open(r'Кызылординская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Мангистауская область":
        bot.send_document(message.from_user.id, open(r'Мангистауская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Павлодарская область":
        bot.send_document(message.from_user.id, open(r'Павлодарская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Северо-Казахстанская область":
        bot.send_document(message.from_user.id, open(r'Северо-Казахстанская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Туркестанская область":
        bot.send_document(message.from_user.id, open(r'Туркестанская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)
    elif message.text == "Назад":
        bot.send_message(message.from_user.id, "Вернуться в главное меню?", reply_markup=lmenu)
        bot.register_next_step_handler(message, ruslanguage)

@bot.message_handler(func=lambda message:True)
def kazcliniclist(message):
    but = types.KeyboardButton("Ақмола облысы")
    but1 = types.KeyboardButton("Ақтөбе облысы")
    but2 = types.KeyboardButton("Алматы облысы")
    but3 = types.KeyboardButton("Атырау облысы")
    but4 = types.KeyboardButton("Шығыс Қазақстан облысы")
    but5 = types.KeyboardButton("Алматы қ.")
    but6 = types.KeyboardButton("Астана қ.")
    but7 = types.KeyboardButton("Шымкент қ.")
    but8 = types.KeyboardButton("Жамбыл облысы")
    but9 = types.KeyboardButton("Батыс Қазақстан облысы")
    but10 = types.KeyboardButton("Қарағанды облысы")
    but11 = types.KeyboardButton("Қостанай облысы")
    but12 = types.KeyboardButton("Қызылорда облысы")
    but13 = types.KeyboardButton("Маңғыстау облысы")
    but14 = types.KeyboardButton("Павлодар облысы")
    but15 = types.KeyboardButton("Оңтүстік Қазақстан облысы")
    but16 = types.KeyboardButton("Түркістан облысы")
    but17 = types.KeyboardButton("Шығу")
    regions = types.ReplyKeyboardMarkup(resize_keyboard=True)
    regions.add(but)
    regions.add(but1)
    regions.add(but2)
    regions.add(but3)
    regions.add(but4)
    regions.add(but5)
    regions.add(but6)
    regions.add(but7)
    regions.add(but8)
    regions.add(but9)
    regions.add(but10)
    regions.add(but11)
    regions.add(but12)
    regions.add(but13)
    regions.add(but14)
    regions.add(but15)
    regions.add(but16)
    regions.add(but17)
    bot.send_message(message.from_user.id, "Облыс/қала таңдаңыз:", reply_markup=regions)
    bot.register_next_step_handler(message, kazcliniclisthandler)

@bot.message_handler(func=lambda message:True)
def kazcliniclisthandler(message):
    lbut = types.KeyboardButton("Да")
    lmenu = types.ReplyKeyboardMarkup(resize_keyboard=True)
    lmenu.add(lbut)
    if message.text == "Ақмола облысы":
        bot.send_document(message.from_user.id, open(r'Акмолинская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Ақтөбе облысы":
        bot.send_document(message.from_user.id, open(r'Актюбинская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Алматы облысы":
        bot.send_document(message.from_user.id, open(r'Алматинская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Атырау облысы":
        bot.send_document(message.from_user.id, open(r'Атырауская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Шығыс Қазақстан облысы":
        bot.send_document(message.from_user.id, open(r'Восточно-Казахстанская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Алматы қ.":
        bot.send_document(message.from_user.id, open(r'г. Алматы.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Астана қ.":
        bot.send_document(message.from_user.id, open(r'г. Астана.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Шымкент қ.":
        bot.send_document(message.from_user.id, open(r'г. Шымкент.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Жамбыл облысы":
        bot.send_document(message.from_user.id, open(r'Жамбылская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Батыс Қазақстан облысы":
        bot.send_document(message.from_user.id, open(r'Западно-Казахстанская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Қарағанды облысы":
        bot.send_document(message.from_user.id, open(r'Карагандинская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Қостанай облысы":
        bot.send_document(message.from_user.id, open(r'Костанайская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Қызылорда облысы":
        bot.send_document(message.from_user.id, open(r'Кызылординская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Маңғыстау облысы":
        bot.send_document(message.from_user.id, open(r'Мангистауская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Павлодар облысы":
        bot.send_document(message.from_user.id, open(r'Павлодарская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Оңтүстік Қазақстан облысы":
        bot.send_document(message.from_user.id, open(r'Северо-Казахстанская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Түркістан облысы":
        bot.send_document(message.from_user.id, open(r'Туркестанская область.docx', 'rb'))
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)
    elif message.text == "Шығу":
        bot.send_message(message.from_user.id, "Негізгі бөлімге оралу?", reply_markup=lmenu)
        bot.register_next_step_handler(message, kazlanguage)


bot.infinity_polling()

