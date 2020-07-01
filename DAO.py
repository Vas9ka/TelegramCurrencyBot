def parse(data):
    currency = ""
    city = ""
    if data[0] == "доллар":
        currency = "USD"
    elif data[0] == "евро":
        currency = "EUR"
    elif data[0] == "юан":
        currency = "CNY"
    elif data[0] == "фунт":
        currency = "GBP"                      
    elif data[0] == "йен":
        currency = "JPY"
    if data[1] == "саратов":
        city = "saratov"
    elif data[1] == "москв":
        city = "moskva"
    elif data[1] == "санкт-петербург" or data[1] == "питер":
        city = "sankt-peterburg"
    elif data[1] == "казан":
        city = "kazan"
    elif data[1] == "екатеринбург":
        city = "ekaterinburg"
    elif data[1] == "нижн":
        city = "nizhniy-novgorod"
    elif data[1] == "новосибирск":
        city = "novosibirsk"
    elif data[1] == "самар":
        city = "samara"
    elif data[1] == "ростове-на дону":
        city = "rostov-na-donu"
    elif data[1] == "красноярск":
        city = "krasnoyarsk"
    elif data[1] == "воронеж":
        city = "voronezh"
    elif data[1] == "краснодар":
        city = "krasnodar"
    elif data[1] == "тюмен":
        city = "tumen"
    elif data[1] == "ижевск":
        city = "izhevsk"
    elif data[1] == "иркутск":
        city = "irkutsk"
    elif data[1] == "хабаровск":
        city = "habarovsk"



    return currency,city
