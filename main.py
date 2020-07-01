
import telebot # Библиотека для работы с ботом Telegram
import CentralBank
import re
import DAO
import Parser
bot = telebot.TeleBot('823117907:AAEU99Ik6rGmFX3fC5pZPVUJC8uP7XNhAVA') # Наш уникальный токен для бота полученый от FatherBot в Telegram
cb = CentralBank.CentralBank()
parser = Parser.Parser()
@bot.message_handler(commands=['start']) # Обработчик команды /start
def start_message(message):
    bot.send_message(message.chat.id, 'Привет! Этот бот может выводить информацию по курсам валют ЦБ РФ и 5 банков региона! Для дополнительной информации напиши /help')

@bot.message_handler(commands=['help']) # Обработчик команды /help
def help_message(message):
    bot.send_message(message.chat.id,
    'Чтобы начать работу с ботом напиши любую фразу содержающую город и валюту, например: "Какой курс юаня в Москве?\n"' +
    "Бот поддерживает inline работу по Центральному Банку, введи в любом чате @another_currency_bot <валюта> <дата> .")

@bot.message_handler(content_types = ['text'])
def get_text_messages(message):
    if message.chat.type == "private":
        string = str(message.text).lower()
        result = re.findall(r'доллар|евро|юан|фунт|йен|',string)
        result += re.findall(r'саратов|москв|санкт-петербург|казан|питер|екатеринбург' +
            r'|нижн|новосибирск|самар|ростове-на-дону|красноярск|воронеж|краснодар|' +
            r'тюмен|ижевск|иркутск|хабаровск',string)
        result = list(filter(lambda a: a != '',result))
        print(result)
        if len(result) < 2:
            bot.send_message(message.chat.id,"Прости по твоему запросу ничего не удалось найти(")
        else:
            currency,city = DAO.parse(result)
            print(currency,city)
            bot.send_message(message.chat.id,parser.GetCurrency(currency,city))
    elif message.chat.type == "group":
        string = str(message.text).lower()
        ifbot = re.findall(r'бот,скажи|эй,бот|эй, бот|бот, скажи',string)
        if(len(ifbot) > 0):
            result = re.findall(r'доллар|евро|юан|фунт|йен|',string)
            result += re.findall(r'саратов|москв|санкт-петербург|казан|питер|екатеринбург' +
                r'|нижн|новосибирск|самар|ростове-на-дону|красноярск|воронеж|краснодар|' +
                r'тюмен|ижевск|иркутск|хабаровск',string)
            result = list(filter(lambda a: a != '',result))
            print(result)
            if len(result) < 2:
                bot.send_message(message.chat.id,"Прости по твоему запросу ничего не удалось найти(")
            else:
                currency,city = DAO.parse(result)
                print(currency,city)
                bot.send_message(message.chat.id,parser.GetCurrency(currency,city))

@bot.message_handler(content_types=["sticker"])
def handle_sticker(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,"\U0001F44D")
    
@bot.message_handler(content_types=["photo"])
def handle_photo(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,"\U0001F44D \n nice фото, awesome пиксели")

@bot.message_handler(content_types=["audio"])
def handle_audio(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,"\U0001F44D \n nice аудио, awesome битрейт")

@bot.message_handler(content_types=["document"])
def handle_document(message):
    if message.chat.type == "private":
        bot.send_message(message.chat.id,"\U0001F44D \n nice документ, awesome шрифт")

@bot.inline_handler(func=lambda query: True)  
def query_text(inline_query):  
    bot.answer_inline_query(  
        inline_query.id,  
        get_iq_articles(cb.get_exchanges(inline_query.query))  
    )
def get_iq_articles(exchanges):
    result = []
    for exc in exchanges:
        result.append(
            telebot.types.InlineQueryResultArticle(
                id = exc,
                title = exc,
                input_message_content=telebot.types.InputTextMessageContent(
                     "RUB -> " + exc + "\n" 
                        + exchanges[exc] + " руб" + "\n"
                ),
                description= ' Convert RUB ' + '-> ' + exc,
                thumb_height=1
            )
        )
    return result

bot.polling(none_stop= True,interval= 0)