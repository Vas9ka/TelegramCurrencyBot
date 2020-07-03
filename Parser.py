import requests
import Logs
from bs4 import BeautifulSoup
def GetCurrency(currency,city):
    URL = 'https://ru.myfin.by/currency'
    counter = 0
    buy = True
    URL += '/' + currency
    URL += '/' + city
    request = requests.get(URL).text
    soup = BeautifulSoup(request)
    result = ""
    try:
        result += soup.h2.text + "\n"
        for tag in soup.find('tbody').find_all('td', ['bank_name',currency]):
            if(tag['class'][0] == "bank_name"):
                if counter == 5:
                    break
                counter += 1
                result += tag.text + "\n"
            if(tag['class'][0] == currency):
                if(buy):
                    result += "Покупка: " + tag.text + " руб.\n"
                    buy = False
                else:
                    result += "Продажа: " + tag.text + " руб. \n"
                    buy = True
        return result
    except AttributeError:
        Logs.log_exception(AttributeError)
        return "Прости, мне ничего не удалось найти :("
