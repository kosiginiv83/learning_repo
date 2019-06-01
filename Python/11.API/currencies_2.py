import osa
from math import ceil
import sys


def cost_calculation(money_dict):
    print(money_dict)
    rub_list = []
    client = osa.Client('http://fx.currencysystem.com/webservices/CurrencyServer4.asmx?WSDL')
    for curr, amount in money_dict.items():
        res = client.service.ConvertToNum(fromCurrency=curr.lower(),
                                          toCurrency='rub',
                                          amount=amount,
                                          rounding=False
                                          )
        rub_list.append(ceil(res))
    print(rub_list)
    print('Сумма в рублях:', sum(rub_list))


def main(file):
    money_dict = {}
    with open(file) as f:
        for line in f:
            item = line.split()
            money_dict[item[2]] = int(item[1])
    cost_calculation(money_dict)


if __name__ == '__main__':
    file = sys.argv[1]
    main(file)