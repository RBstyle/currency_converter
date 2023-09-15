import requests
import json


def converter(from_input, to_input, value_input):
    response = requests.get("https://www.cbr-xml-daily.ru/daily_json.js")
    result = json.loads(response.text)

    value = check_value(value_input)
    from_currency = check_currency(from_input, result)
    to_currency = check_currency(to_input, result)

    if from_currency and to_currency and value:
        total = (from_currency / to_currency) * value
    else:
        return "Wrong input!"
    return {"result": total}


def check_currency(currency, valutes_dict):
    if currency == "RUB":
        return 1
    elif not valutes_dict["Valute"].get(currency):
        return False
    result = valutes_dict["Valute"].get(currency).get("Value")
    nominal = valutes_dict["Valute"].get(currency).get("Nominal")
    return result / nominal


def check_value(value_input):
    try:
        result = float(value_input)
    except:
        return False
    return result
