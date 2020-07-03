import CentralBank
def test_date_and_currency_cb():
    assert  CentralBank.GetCurrency("USD","20-03-2000") == "Курсы валют ЦБ РФ на 20 марта 2000 (USD)\n28.41 руб."
    assert CentralBank.GetCurrency("UZM","20-03-2000") == None
def test_currency_cb():
    assert CentralBank.GetCurrency("USD") == "Курсы валют ЦБ РФ на сегодня (USD)\n70.5198 руб."
    assert CentralBank.GetCurrency("UZM") == None
