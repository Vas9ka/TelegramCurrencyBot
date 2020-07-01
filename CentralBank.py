import requests
import xml.etree.ElementTree as ET
import re
class CentralBank:
    URL = 'http://www.cbr.ru/scripts/XML_daily.asp?'

    def load_exchange(self):
        root  = ET.fromstring(requests.get(self.URL).text)
        currencies = {}
        for i in range(len(root)):
           currencies[root[i][1].text] = str(float(root[i][4].text.replace(',','.')) / float(root[i][2].text))
        return currencies

    def get_exchange(self,currency):
        return self.load_exchange()[currency]
    def get_exchanges(self,ccy_pattern):  
        result = {}
        ccy_pattern = re.escape(ccy_pattern) + '.*' 
        currencies = self.load_exchange() 
        for exc in currencies:  
            if re.match(ccy_pattern, exc, re.IGNORECASE) is not None:
                result[exc] = currencies[exc]
        return result
