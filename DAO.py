def parse(data):
    cities = {}
    cities['благовещенск'] = 'amurskaya-oblast-blagoveschensk'
    cities['архангельск'] = 'arhangelsk'
    cities['астрахан'] = 'astrahan'
    cities['белгород'] = 'belgorod'
    cities['брянск'] = 'bryansk'
    cities['владимир'] = 'vladimir'
    cities['волгоград'] = 'volgograd'
    cities['вологд'] = 'vologda'
    cities['воронеж'] = 'voronezh'
    cities['иваново'] = 'ivanovo'
    cities['иркутск'] = 'irkutsk'
    cities['калининград'] = 'kaliningrad'
    cities['калуга'] = 'kaluga'
    cities['петропавловске-камчатский'] = 'petropavlovsk-kamchatskiy'
    cities['кемерово '] = 'kemerovo'
    cities['киров'] = 'kirovskaya-oblast-kirov'
    cities['костром'] = 'kostroma'
    cities['курган'] = 'kurgan'
    cities['курск'] = 'kursk'
    cities['санкт-петербург'] = 'sankt-peterburg'
    cities['питер'] = 'sankt-peterburg'
    cities['липецк'] = 'lipeck'
    cities['магадан'] = 'magadan'
    cities['москв'] = 'moskva'
    cities['мурманск'] = 'murmansk'
    cities['нижн'] = 'nizhniy-novgorod'
    cities['велик'] = 'velikiy-novgorod'
    cities['новосибирск'] = 'novosibirsk'
    cities['омск'] = 'omsk'
    cities['оренбург'] = 'orenburg'
    cities['пенз'] = 'penza'
    cities['перм'] = 'perm'
    cities['псков'] = 'pskov'
    cities['ростове-на-дону'] = 'rostov-na-donu'
    cities['рязан'] = 'ryazan'
    cities['самар'] = 'samara'
    cities['саратов'] = 'saratov'
    cities['южно-сахалинск'] = 'yuzhno-sahalinsk'
    cities['екатеринбург'] = 'ekaterinburg'
    cities['смоленск'] = 'smolensk'
    cities['тамбов'] = 'tambov'
    cities['тул'] = 'tula'
    cities['тюмен'] = 'tumen'
    cities['ульяновск'] = 'ulyanovsk'
    cities['челябинск'] = 'chelyabinsk'
    cities['чит'] = 'chita'
    cities['ярославл'] = 'yaroslavl'
    cities['майкоп'] = 'maykop'
    cities['горно-алтайск'] = 'gorno-altaysk'
    cities['уф'] = 'ufa'
    cities['улан-уде'] = 'ulan-ude'
    cities['махачкал'] = 'mahachkala'
    cities['биробиджан'] = 'birobidzhan'
    cities['нальчик'] = 'nalchik'
    cities['элист'] = 'elista'
    cities['черкесск'] = 'cherkessk'
    cities['петрозаводск'] = 'petrozavodsk'
    cities['сыктывкар'] = 'siktivkar'
    cities['симферопол'] = 'simferopol'
    cities['йошкар-ол'] = 'yoshkar-ola'
    cities['саранск'] = 'saransk'
    cities['якутск'] = 'yakutsk'
    cities['владикавказ'] = 'vladikavkaz'
    cities['казан'] = 'kazan'
    cities['кызыл'] = 'kizil'
    cities['ижевск'] = 'izhevsk'
    cities['абакан'] = 'abakan'
    cities['грозн'] = 'grozniy'
    cities['чебоксар'] = 'cheboksari'
    cities['барнаул'] = 'barnaul'
    cities['краснодар'] = 'krasnodar'
    cities['красноярск'] = 'krasnoyarsk'
    cities['владивосток'] = 'vladivostok'
    cities['ставропол'] = 'stavropol'
    cities['хабаровск'] = 'habarovsk'
    cities['нарьян-Мар'] = 'naryan-mar'
    cities['ханты-мансийск'] = 'hanti-mansiysk'
    cities['анадыр'] = 'anadir'
    cities['салехард'] = 'salehard'
    currency = ""
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
    if(len(data) == 1):
        return currency
    if(data[1][0].isnumeric()):
        return currency
    city = cities[data[1]]

    return currency,city
