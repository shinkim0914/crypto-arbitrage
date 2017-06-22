import requests

# CB stands for Coinbase
# BH stands for Bithumb

# Takes cryptocurrency code (e.g. 'BTC', 'ETH', 'LTC') as input and returns dictionary of Coinbase (U.S.) price, Bithumb (Korea) price, and the spread between the two
def GetPrice(cryptocurrency):
    CBPriceRequest = requests.get('https://api.coinbase.com/v2/prices/'+cryptocurrency+'-USD/spot')
    CBPriceUSD = float(CBPriceRequest.json()['data']['amount'])

    BHPriceRequest = requests.get('https://api.bithumb.com/public/recent_transactions/'+cryptocurrency)
    BHPriceKRW = float(BHPriceRequest.json()['data'][0]['price'])

    USDKRWRequest = requests.get('http://api.fixer.io/latest?base=USD&symbols=KRW')
    KRWUSD = USDKRWRequest.json()['rates']['KRW']

    BHPriceUSD = BHPriceKRW / KRWUSD
    return {'Currency': cryptocurrency, 'CB': CBPriceUSD, 'BH': BHPriceUSD, 'Spread': BHPriceUSD/CBPriceUSD-1}

print(GetPrice('BTC'))
print(GetPrice('ETH'))
print(GetPrice('LTC'))