import telebot
from telebot import types
from geopy.geocoders import Nominatim


bot =telebot.TeleBot('1372088219:AAEFWaIZq_tbzQ8MWoqA3YIt2MgcTGuYAUg')

data = {'contact': "", 'type': "", 'weight': ""}

bot.state = None # create own value `.state` in `bot` - so I don't have to use `global state`. Similar way I could create and use `bot.data`


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 =types.KeyboardButton('Kontakt 📲', request_contact=True)
    markup.add(btn1)
    send_mess = f"<b>Salom, {message.from_user.first_name}! </b> \nBuyurtma berishdan avval o'z kontaklaringiz bilan ulashing!"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    global user_id
    user_id = message.from_user.id



@bot.message_handler(content_types=['contact'])
def mess(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    btn1 =types.KeyboardButton('Lokatsiya 📍', request_location=True)
    btn2 = types.KeyboardButton("O'tkazib yuborish ➡️")
    markup.add(btn1, btn2)
    send_mess = f"Rahmat, davom etish uchun lokatsiyani ham ulashing"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=markup)
    data['contact'] = message.contact.phone_number
    global user_number
    user_number = message.contact.phone_number

@bot.message_handler(content_types=['location'])
def mess(message):
    send_mess = f"<b>Rahmat {message.from_user.first_name} </b>!"
    bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=mainkeyboard)
    coord = (message.location.latitude, message.location.longitude)
    geolocator = Nominatim(user_agent="main.py")
    location = geolocator.reverse(f'{coord[0]}, {coord[1]}')
    data['type'] = location.address
    msg = "<b>Имя:</b> {}  \n<b>Номер:</b> {} \n<b>Адрес:</b> {} ".format(message.from_user.first_name,  data['contact'], data['type'])
    bot.send_message(-452474686, msg, parse_mode='html')
    bot.send_location(-452474686, message.location.latitude, message.location.longitude)


global mainkeyboard
global keyboard

keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2, one_time_keyboard=True)
btn1 = types.KeyboardButton('1kg')
btn2 = types.KeyboardButton('5kg')
btn3 = types.KeyboardButton('10kg')
btn4 = types.KeyboardButton("20kg")
btn5 = types.KeyboardButton("50kg")
btn6 = types.KeyboardButton("Boshqasi")
btn7 = types.KeyboardButton('Bekor qilish ❌')
keyboard.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)

mainkeyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
btn1 = types.KeyboardButton('Mahsulotlarimiz 🐛')
btn2 = types.KeyboardButton('Bizning manzilimiz 📍')
btn3 = types.KeyboardButton("Bog'lanish uchun ☎️")
btn4 = types.KeyboardButton('Vitae.uz ✅')
mainkeyboard.add(btn1, btn2, btn3, btn4)


order = {'product': "", 'weight': ""}


@bot.message_handler(content_types=['text'])
def mess(message):
    get_message_bot = message.text.strip().lower()

    if get_message_bot == "o'tkazib yuborish ➡️":
        send_mess = f"<b>Rahmat {message.from_user.first_name} </b>!"
        bot.send_message(message.chat.id, send_mess, parse_mode='html', reply_markup=mainkeyboard)
        msg = "<b>Имя:</b> {}  \n<b>Номер:</b> {} ".format(message.from_user.first_name, data['contact'])
        bot.send_message(-452474686, msg, parse_mode='html')
    elif get_message_bot == "ortga qaytish ⬅️":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Qora lvinkaning tirik lichinkasi')
        btn2 = types.KeyboardButton('Quritilgan lichinka')
        btn3 = types.KeyboardButton('Proteinli konsentrat «Germecia»')
        btn4 = types.KeyboardButton("Organik o'g'it «Germecia» Biohumus")
        btn5 = types.KeyboardButton("Yog'li «Germecia»")
        btn6 = types.KeyboardButton('Boshiga ⬅️')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        final_message = "Sizni nima qiziqtirmoqda?"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "boshiga ⬅️":
        final_message = "Sizni nima qiziqtirmoqda?"
        bot.send_message(message.chat.id, final_message, parse_mode='html', reply_markup=mainkeyboard)
    elif get_message_bot == "bizning manzilimiz 📍":
        manzil = "Toshkent tumani, Taraqqiy ko’chasi"
        bot.send_message(message.chat.id, manzil,)
        bot.send_location(message.chat.id, 41.436964, 69.372849)
    elif get_message_bot == "bog'lanish uchun ☎️":
        telefon = f"<b>Телефон:</b>\n+99899 871-17-04 \n+99890 319-62-68\n\n" \
                  f"<b>E-mail:</b>\ninfo@vitae.uz"
        bot.send_message(message.chat.id, telefon, parse_mode='html')
    elif get_message_bot == "mahsulotlarimiz 🐛":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
        btn1 = types.KeyboardButton('Qora lvinkaning tirik lichinkasi')
        btn2 = types.KeyboardButton('Quritilgan lichinka')
        btn3 = types.KeyboardButton('Proteinli konsentrat «Germecia»')
        btn4 = types.KeyboardButton("Organik o'g'it «Germecia» Biohumus")
        btn5 = types.KeyboardButton("Yog'li «Germecia»")
        btn6 = types.KeyboardButton('Buyurtma berish 📌')
        btn7 = types.KeyboardButton('Boshiga ⬅️')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
        finaal_message = "Sizni nima qiziqtirmoqda??"
        bot.send_message(message.chat.id, finaal_message, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "vitae.uz ✅":
        p = open("images/vita.jpg", 'rb')
        about = "<b>Kuniga 10.000kg ozuqa xomashyosi</b> \n\n" \
                "Bizning ishlab chiqarish quvvatlarimiz kuniga 10 tonnagacha ozuqa xomashyosini qayta ishlashga imkon beradi. " \
                "Shunday qilib, biz O’zbekistondagi eng yirik qora lichinka baliqlari mahsulotlarini ishlab chiqaruvchilarmiz. " \
                "Faqat o’simlik materiallaridan foydalanish sanitariya va veterinariya me’yorlariga javob beradigan eng xavfsiz mahsulotni olishga imkon beradi. " \
                "Amaldagi texnologiya va uskunalar lichinkaning biologik qiymatini va uni qayta ishlash mahsulotlarini saqlashga imkon beradi \n\n" \
                "<b>✅ Yanada kuchli tuxum po’stlari. Har bir cho’qish bilan 50 barobarko’proq kaltsiy oling.\n\n" \
                "✅ Qurtlar – quritilgan qora askar chivinlari lichinkalari, tovuqlar uchun kunlik sog’lik garovidir.\n\n" \
                "✅ Yaxlitlash osonroq. Ovqatlanish paytida lichinkalarni tuting va muhabbat bilan o’rab oling. ular yugurib kelishadi.</b>"
        bot.send_photo(message.chat.id, p, about, parse_mode='html')

    elif get_message_bot == "quritilgan lichinka":
        p = open("images/ql.jpg", 'rb')
        info = "<b>Quritilgan lichinka:</b>\n\n" \
               "<b>Tavsif:</b> Qora lvinkaning (Hermetia illusens) quritilgan butun lichinkasi\n\n" \
               "<b>Tarkibi:</b> 100% qora lvinka lichinkalaridan iborat\n\n" \
               "<b>Ilova:</b> U qishloq xo’jaligi hayvonlari, parrandalar, suv xo’jaligi va mahsuldor bo’lmagan hayvonlar uchun ozuqada oqsil, yog ‘va uglevodlarning manbai sifatida ishlatiladi.\n\n" \
               "<b>Jismoniy xususiyatlari:</b>\n\n" \
               "<b>Hidi:</b> o’ziga xos, qattiq emas, chirigan emas, yumshoq rang.\n" \
               "<b>Rangi:</b> Kulrangdan jigarranggacha.\n" \
               "<b>Xavfsizlik ko’rsatkichlari:</b> Toksik emas Anaeroblar – yo’q\n" \
               "<b>Salmonella</b> – yo’q\n" \
               "<b>Escherichia coli</b> – yo’q\n" \
               "<b>Proteus</b> – yo’q\n" \
               "<b>Qadoq:</b>…, …, …, litr sumkalar\n\n" \
               "<b>Saqlash muddati:</b> 12 oy"
        bot.send_photo(message.chat.id, p, info, parse_mode='html')
    elif get_message_bot == "qora lvinkaning tirik lichinkasi":
        p = open("images/tk.jpg", 'rb')
        info = "<b>Tirik Lichinka:</b>\n\n" \
               "<b>Tavsif:</b> Qora lvinkaning jonli lichinkasi( Hermetia illusens). Lichinkaning uzunligi 25 mm gacha, kengligi 5 mm gacha – yoshga qarab.\n\n" \
               "<b>Tarkibi:</b> 100% qora lvinka lichinkalaridan iborat.\n\n" \
               "<b>Ilova:</b> U hasharotlar, qushlar, sudralib yuruvchilar, amfibiyalar va baliqlar uchun jonli ovqat sifatida ishlatiladi. U baliq ovlashda jonli o’lja sifatida ishlatiladi. Baliq ovi uchun ishlatiladigan goʻshtli pashhaga alternativ sifatida. Lichinkani turli yoshlarda olib tashlash orqali biz turli o’lchamdagi lichinkalarni olamiz – 10 dan 25 mm gacha.\n\n" \
               "<b>Jismoniy xususiyatlari:</b>\n\n" \
               "<b>Hid:</b> o’ziga xos, qattiq emas, chirigan emas, yumshoq\n" \
               "<b>Rang:</b> oqdan qora ranggacha.\n" \
               "<b>Xavfsizlik ko’rsatkichlari:</b> toksik bo’lmagan\n" \
               "<b>Anaeroblar</b> – yo’q\n" \
               "<b>Salmonella</b> – yo’q\n" \
               "<b>Escherichia coli</b> - yo’q\n" \
               "<b>Proteus</b> – yo’q\n" \
               "<b>Qadoq:</b>  … ml idishlar\n\n" \
               "<b>Saqlash shartlari:</b> Voyaga yetgan va undan avvaligi prepupani 4 haftagacha 8-120C haroratda saqlang.\n\n" \
               "Yosh lichinkalarni 2 oygacha 10-250C haroratda saqlang"
        bot.send_photo(message.chat.id, p, info, parse_mode='html')
    elif get_message_bot == "proteinli konsentrat «germecia»":
        p = open("images/pk.jpg", 'rb')
        info = "<b>Proteinli konsentrat «Germecia»</b>\n\n" \
               "<b>Tavsif:</b> Qora lvinka qurtlari (Hermetia illucens) quritilgan yog’sizlangan va maydalangan biomassasi. Quritish infraqizil qurilmalarda barcha biologik faol xususiyatlarni saqlab qolish bilan amalga oshiriladi.\n\n"\
               "<b>Tarkibi:</b> Antioksidant bo’lgan qora sher lichinkalarining kam yog’li biomassasi.\n\n" \
               "<b>Ilova:</b> Makro va mikroelementlar manbai, tuproqni yaxshilagich sifatida ishlatiladi. Foydasi kam tuproqlarni foydali mikroflora bilan boyitadi.\n\n" \
               "<b>Jismoniy xususiyatlari:</b>\n\n" \
               "<b>Hidi:</b> kuchli emas, oʻtkir emas, chirigan hid kelmaydi\n" \
               "<b>Rang:</b> kulrangdan jigarranggacha.\n" \
               "<b>Shakli:</b> qumsimon va granular\n" \
               "<b>Xavfsizlik ko’rsatkichlari:</b> Toksik bo’lmagan\n" \
               "<b>Anaeroblar</b> – yo’q\n" \
               "<b>Salmonella</b> – yo’q\n" \
               "<b>Escherichia coli</b> – yo’q\n" \
               "<b>Proteus</b> – yo’q\n" \
               "<b>Qadoq:</b> 10-40 kg lik qoplarda\n\n" \
               "<b>Saqlash muddati:</b> 12 oy"
        bot.send_photo(message.chat.id, p, info, parse_mode='html')
    elif get_message_bot == "organik o'g'it «germecia» biohumus":
        p = open("images/oo.png", 'rb')
        info = "<b>Organik o'g'it «Germecia» Biohumus:</b>\n\n" \
               "<b>Tavsif:</b> Qora lvinka (Hermetia illusens) lichinkasining quritilgan, yogʻsizlantirilgan va maydalangan biomassasi. Quritish barcha biologik xususiyatlarni saqlab qilgan holda infro qizil qurilmalarda amalga oshiriladi.\n\n" \
               "<b>Tarkibi:</b> Qora lvinka lichinkalarining yogʻsizlantirilgan biomassasi, antioksidant.\n\n" \
               "<b>Qo’llash:</b> Qishloq xoʻjaligi hayvonlari, parrandalar, suv hayvonlarini va uy hayvonlari uchun moʻljallangan ozuqada oqsil, yogʻ va biologik faol moddalar manbai sifatida qoʻllaniladi.\n\n" \
               "<b>Jismoniy xususiyatlari:</b>\n\n" \
               "<b>Hidi:</b> o’ziga xos, yoqimli.\n" \
               "<b>Rang:</b> kulrangdan jigarranggacha.\n" \
               "<b>Xavfsizlik ko’rsatkichlari:</b>  Toksik emas – yo’q mavjud emas\n" \
               "<b>Anaeroblar</b> – yo’q\n" \
               "<b>Salmonella</b> – yo’q\n" \
               "<b>Escherichia coli</b> – yo’q\n" \
               "<b>Proteus</b> – yo’q\n" \
               "<b>Qadoq:</b> 10-40 kg lik qoplarda\n\n" \
               "<b>Saqlash muddati:</b> 12 oy"
        bot.send_photo(message.chat.id, p, info, parse_mode='html')
    elif get_message_bot == "yog'li «germecia»":
        p = open("images/yh.jpg", 'rb')
        info = "<b>Yog'li «Hermecia»:</b>\n\n" \
               "<b>Tavsif:</b> Qora lichinka yog’i lichinka biomassasidan yog ‘bosish va ajratish yo’li bilan olinadi.\n\n" \
               "<b>Tarkibi:</b> Qora lichinka lichinkalaridan 100% yog ‘mavjud\n\n" \
               "<b>Ilova:</b> Bu ozuqa ishlab chiqarish, sovun tayyorlash, kosmetologiya va farmatsevtika sohasida foydalanish uchun tavsiya etiladi.\n\n" \
               "<b>Jismoniy xususiyatlari:</b>\n\n" \
               "<b>Erish nuqtasi:</b> 400S\n" \
               "<b>Hidi:</b> o’ziga xos, qattiq emas, chirigan emas, yumshoq\n" \
               "<b>Rang:</b> oqdan jigarranggacha.\n" \
               "<b>Xavfsizlik ko’rsatkichlari:</b> Toksik bo’lmagan\n" \
               "<b>Anaeroblar</b> – yo’q\n" \
               "<b>Salmonella</b> – yo’q\n" \
               "<b>Escherichia coli</b> – yo’q\n" \
               "<b>Proteus</b> – yo’q\n" \
               "<b>Qadoq:</b> litr bochkalari\n\n" \
               "<b>Saqlash muddati:</b>12 oy"
        bot.send_photo(message.chat.id, p, info, parse_mode='html')
    elif get_message_bot == "buyurtma berish 📌":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Qora lvinkaning tirik lichinkasi.')
        btn2 = types.KeyboardButton('Quritilgan lichinka.')
        btn3 = types.KeyboardButton('Proteinli konsentrat «Germecia».')
        btn4 = types.KeyboardButton("Organik o'g'it «Germecia» Biohumus.")
        btn5 = types.KeyboardButton("Yog'li «Germecia».")
        btn6 = types.KeyboardButton('Bekor qilish ❌')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        messa = "Marxamat mahsulotni tanlang"
        bot.send_message(message.chat.id, messa, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "bekor qilish ❌":
        msg = "Bekor qilindi"
        bot.send_message(message.chat.id, msg, reply_markup=mainkeyboard )
    elif get_message_bot == "qora lvinkaning tirik lichinkasi.":
        messa = "Buyurtma hajmini tanlang"
        bot.send_message(message.chat.id, messa, parse_mode='html', reply_markup=keyboard)
        order['product'] = message.text
    elif get_message_bot == "quritilgan lichinka.":
        messa = "Buyurtma hajmini tanlang"
        bot.send_message(message.chat.id, messa, parse_mode='html', reply_markup=keyboard)
        order['product'] = message.text
    elif get_message_bot == "proteinli konsentrat «germecia».":
        messa = "Buyurtma hajmini tanlang"
        bot.send_message(message.chat.id, messa, parse_mode='html', reply_markup=keyboard)
        order['product'] = message.text
    elif get_message_bot == "organik o'g'it «germecia» biohumus.":
        messa = "Buyurtma hajmini tanlang"
        bot.send_message(message.chat.id, messa, parse_mode='html', reply_markup=keyboard)
        order['product'] = message.text
    elif get_message_bot == "yog'li «germecia».":
        messa = "Buyurtma hajmini tanlang"
        bot.send_message(message.chat.id, messa, parse_mode='html', reply_markup=keyboard)
        order['product'] = message.text
    elif get_message_bot == "1kg":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Tasdiqlash")
        btn2 = types.KeyboardButton("Bekor qilish ❌")
        markup.add(btn1, btn2)
        order['weight'] = message.text
        messag= """<b>Siznining buyurmangiz</b>📎\n\n<b>Mahsulot:</b>  {}\n\n<b>Hajmi</b>:  {}""".format(order['product'], order['weight'])
        bot.send_message(message.chat.id, messag, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "5kg":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Tasdiqlash")
        btn2 = types.KeyboardButton("Bekor qilish ❌")
        markup.add(btn1, btn2)
        order['weight'] = message.text
        messag = """<b>Siznining buyurmangiz</b>📎\n\n<b>Mahsulot:</b>  {}\n\n<b>Hajmi</b>:  {}""".format(
            order['product'], order['weight'])
        bot.send_message(message.chat.id, messag, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "10kg":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Tasdiqlash")
        btn2 = types.KeyboardButton("Bekor qilish ❌")
        markup.add(btn1, btn2)
        order['weight'] = message.text
        messag= """<b>Siznining buyurmangiz</b>📎\n\n<b>Mahsulot:</b>  {}\n\n<b>Hajmi</b>:  {}""".format(order['product'], order['weight'])
        bot.send_message(message.chat.id, messag, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "20kg":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Tasdiqlash")
        btn2 = types.KeyboardButton("Bekor qilish ❌")
        markup.add(btn1, btn2)
        order['weight'] = message.text
        messag= """<b>Siznining buyurmangiz</b>📎\n\n<b>Mahsulot:</b>  {}\n\n<b>Hajmi</b>:  {}""".format(order['product'], order['weight'])
        bot.send_message(message.chat.id, messag, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "50kg":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Tasdiqlash")
        btn2 = types.KeyboardButton("Bekor qilish ❌")
        markup.add(btn1, btn2)
        order['weight'] = message.text
        messag = """<b>Siznining buyurmangiz</b>📎\n\n<b>Mahsulot:</b>  {}\n\n<b>Hajmi</b>:  {}""".format(
            order['product'], order['weight'])
        bot.send_message(message.chat.id, messag, parse_mode='html', reply_markup=markup)
    elif get_message_bot == "boshqasi":
        mess = bot.send_message(message.chat.id, "Kerakli bo'lgan hajimni kiriting")
        bot.register_next_step_handler(mess, get_custom_weight)
    elif get_message_bot == "tasdiqlash":
        mes = "Yana buyurtma berasizmi?"
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton("Ha, albatta")
        btn2 = types.KeyboardButton("Bekor qilish ❌")
        markup.add(btn1,btn2)
        buyurtma= """<b>Buyurtma</b>📎\n\n<b>Buyurtmachi:</b>  {}\n<b>Telefon raqami:</b>  {}\n<b>Mahsulot:</b>  {}\n<b>Hajmi</b>:  {}""".format(message.from_user.first_name, data['contact'], order['product'], order['weight'])
        bot.send_message(message.chat.id, mes, reply_markup=markup)
        bot.send_message(-452474686, buyurtma, parse_mode='html')
        bot.state = None
    elif get_message_bot == "ha, albatta":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
        btn1 = types.KeyboardButton('Qora lvinkaning tirik lichinkasi.')
        btn2 = types.KeyboardButton('Quritilgan lichinka.')
        btn3 = types.KeyboardButton('Proteinli konsentrat «Germecia».')
        btn4 = types.KeyboardButton("Organik o'g'it «Germecia» Biohumus.")
        btn5 = types.KeyboardButton("Yog'li «Germecia».")
        btn6 = types.KeyboardButton('Bekor qilish ❌')
        markup.add(btn1, btn2, btn3, btn4, btn5, btn6)
        messa = "Marxamat mahsulotni tanlang"
        bot.send_message(message.chat.id, messa, parse_mode='html', reply_markup=markup)
    else:
        fiinal_message = f"Noaniq so'rov, {message.from_user.first_name} iltimos kerakli yonalishni tanlang"
        bot.send_message(message.chat.id, fiinal_message, parse_mode='html', reply_markup=mainkeyboard)

def get_custom_weight(message):
        age = message.text
        if not age.isdigit():
            msg = bot.reply_to(message, 'Iltimos kerakli hajimni faqat son shaklida kiriting')
            bot.register_next_step_handler(msg, get_custom_weight)
        else:
            order['weight'] = message.text
            markup = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
            btn1 = types.KeyboardButton("Tasdiqlash")
            btn2 = types.KeyboardButton("Bekor qilish ❌")
            markup.add(btn1, btn2)
            messag = """<b>Siznining buyurmangiz</b>📎\n\n<b>Mahsulot:</b>  {}\n\n<b>Hajmi</b>:  {} kg""".format(
            order['product'], order['weight'])
            bot.send_message(message.chat.id, messag, parse_mode='html', reply_markup=markup)

bot.polling(none_stop=True)
#




