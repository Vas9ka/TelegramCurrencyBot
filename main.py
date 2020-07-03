
import telebot # Библиотека для работы с ботом Telegram
import CentralBank
import re
import DAO
import Parser
import Logs
bot = telebot.TeleBot('823117907:AAEU99Ik6rGmFX3fC5pZPVUJC8uP7XNhAVA') 
@bot.message_handler(commands=['start']) 
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Этот бот может выводить информацию по курсам валют ЦБ РФ и 5 банков региона! Для дополнительной информации напиши /help')

@bot.message_handler(commands=['help']) 
def help_message(message):
    bot.send_message(message.chat.id,
    '1.Чтобы начать работу с ботом напиши любую фразу содержающую город и валюту, например: "Какой курс юаня в Москве?"\n' +
    '2.Бота можно добавить в групповой чат, чтобы вызвать его напиши "Эй, бот" и введи свой запрос.\n' +
    '3.Бот может показать значение курса по Центральному банку, в запросе должно быть слово "цб" и валюта. Дату указывать в формате DD-MM-YYYY.\n' +
    'Например, "цб евро 20-03-2005", если не указывать дату, бот выведет информацию о курсе на сегодня')

@bot.message_handler(content_types = ['text']) 
def get_text_messages(message):
    string = str(message.text).lower()
    ifbot = re.findall(r'бот,скажи|эй,бот|эй, бот|бот, скажи',string)

    if message.chat.type == "private" or message.chat.type == "group" and len(ifbot) > 0:
        Logs.log(message)
        result = re.findall(r'доллар|евро|юан|фунт|йен',string)
        result += re.findall(r'саратов|москв|санкт-петербург|казан|питер|екатеринбург' +
            r'|нижн|новосибирск|самар|ростове-на-дону|красноярск|воронеж|краснодар|' +
            r'тюмен|ижевск|иркутск|хабаровск|благовещенск|архангельск|астрахан|белгород|брянск' +
            r'|владимир|волгоград|вологд|иваново|калининград|калуга|петропавловске-камчатский|кемерово' +
            r'|киров|костром|курган|курск|липецк|магадан|мурманск|велик|омск|оренбург|пенз|перм|псков' +
            r'|рязан|южно-сахалинск|смоленск|тамбов|тул|тюмен|ульяновск|челябинск|чит|ярославл|майкоп' +
            r'|горно-алтайск|уф|улан-уде|махачкал|биробиджан|нальчик|элист|черкесск|петрозаводск|сыктывкар|симферопол' +
            r'|йошкар-ол|саранск|якутск|владикавказ|казан|кызыл|ижевск|абакан|грозн|чебоксар|барнаул|краснодар|' +
            r'владивосток|ставропол|нарьян-мар|ханты-мансийск|анадыр|салехард'
            ,string)

        resultcb = re.findall(r'доллар|евро|юан|фунт|йен',string)
        resultcb += re.findall(r'..-..-....',string)
        if len(result) < 2 and len(re.findall(r'цб',string)) == 0 or len(resultcb) == 0 or resultcb[0][0].isnumeric():
            Logs.log(bot.send_message(message.chat.id,"Прости, по твоему запросу ничего не удалось найти("))
        elif len(re.findall(r'цб',string)) != 0 and len(resultcb) != 0:
            date = None
            currency = DAO.parse(resultcb)
            if len(resultcb) == 2:
                date = resultcb[1]
            Logs.log(bot.send_message(message.chat.id,CentralBank.GetCurrency(currency,date)))


        elif(len(result) >= 2):
            currency,city = DAO.parse(result)
            print(currency,city)
            Logs.log(bot.send_message(message.chat.id,Parser.GetCurrency(currency,city)))

@bot.message_handler(content_types=["sticker"]) 
def handle_sticker(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,"\U0001F44D")
        Logs.log(message)
    
@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,"\U0001F44D \n nice фото, awesome пиксели")
        Logs.log(message)


@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,"\U0001F44D \n nice аудио, awesome битрейт")
        Logs.log(message)

@bot.message_handler(content_types=["document"])
def handle_document(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,"\U0001F44D \n nice документ, awesome шрифт")
        Logs.log(message)



bot.polling(none_stop= True,interval= 0)