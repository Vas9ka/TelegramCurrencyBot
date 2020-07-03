import requests
from bs4 import BeautifulSoup
import re
import Logs
def GetCurrency(currency, date = None):
    newcurr = "(" + currency + ")"
    URL = "https://ru.myfin.by/currency/cb-rf"
    if date:
        URL += "/" + date
    request = requests.get(URL).text
    soup = BeautifulSoup(request)
    find = False
    result = ""
    try:
        result += soup.h1.text  + " " + newcurr + "\n"
        for tag in soup.find('tbody').find_all('td'):
            if re.findall(newcurr,tag.text):
                find  = True
                continue
            if find:
                result += tag.text + " руб."
                return result
    except AttributeError:
        Logs.log_exception(AttributeError)
        return "Прости, мне ничего не удалось найти :("

