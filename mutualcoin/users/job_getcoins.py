import requests
import os
import django
from os import sys, path

sys.path.append(path.dirname(path.dirname(path.dirname(path.abspath(__file__)))))
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings.local")
django.setup()

from mutualcoin.users.models import Coin
from datetime import datetime

def get_coins():
    # url = 'https://www.cryptocompare.com/api/data/coinsnapshotfullbyid/?id={}'.format(cid)
    url = 'https://min-api.cryptocompare.com/data/all/coinlist'
    coins = requests.get(url).json()
    for _, coin in coins['Data'].items():            
        try:
            defaults = {
                  'id': coin['Id'],
                  'url': coin.get('Url'),
                  'imageurl': coin.get('ImageUrl'),
                  'name': coin['Name'],
                  'symbol': coin['Symbol'],
                  'coinname': coin['CoinName'],
                  'fullname': coin['FullName'],
                  'algorithm': coin['Algorithm'],
                  'prooftype': coin['ProofType'],
                  'fullypremined': coin['FullyPremined'],
                  'totalcoinsupply': get_number(coin['TotalCoinSupply']),
                  'sortorder': coin['SortOrder'],
                  'sponsored': coin['Sponsored']
                }

            Coin.objects.update_or_create(id=coin['Id'], defaults=defaults)
        except Exception, e:
            print str(e)
            print coin

def get_number(val):
    val = val.replace(',', '').replace(' ', '').replace(u'\u200b', '')
    if val.count('.') > 1:
        val = val.replace('.', '')
    return val if val != 'N/A' else 0

def get_prices():
    coins = [coin.symbol for coin in Coin.objects.all()]
    for i in range(0, len(coins), 50):
        _coins = ','.join([ii for ii in coins[i:i+49]])

        url = 'https://min-api.cryptocompare.com/data/pricemultifull?fsyms={}&tsyms=USD'.format(_coins)
        data = requests.get(url).json()
        for _coin in data['RAW']:
            try:
                Coin.objects.filter(symbol=_coin).update(
                    type=data['RAW'][_coin]['USD']['TYPE'],
                    flags=data['RAW'][_coin]['USD']['FLAGS'],
                    price=data['RAW'][_coin]['USD']['PRICE'],
                    lastupdate=data['RAW'][_coin]['USD']['LASTUPDATE'],
                    lastvolume=data['RAW'][_coin]['USD']['LASTVOLUME'],
                    lastvolumeto=data['RAW'][_coin]['USD']['LASTVOLUMETO'],
                    lasttradeid=data['RAW'][_coin]['USD']['LASTTRADEID'],
                    volumeday=data['RAW'][_coin]['USD'].get('VOLUMEDAY', 0),
                    volumedayto=data['RAW'][_coin]['USD'].get('VOLUMEDAYTO', 0),
                    volume24hour=data['RAW'][_coin]['USD'].get('VOLUME24HOUR', 0),
                    volume24hourto=data['RAW'][_coin]['USD'].get('VOLUME24HOURTO', 0),
                    openday=data['RAW'][_coin]['USD'].get('OPENDAY', 0),
                    highday=data['RAW'][_coin]['USD'].get('HIGHDAY', 0),
                    lowday=data['RAW'][_coin]['USD'].get('LOWDAY', 0),
                    open24hour=data['RAW'][_coin]['USD'].get('OPEN24HOUR', 0),
                    high24hour=data['RAW'][_coin]['USD'].get('HIGH24HOUR', 0),
                    low24hour=data['RAW'][_coin]['USD'].get('LOW24HOUR', 0),
                    lastmarket=data['RAW'][_coin]['USD'].get('LASTMARKET', 0),
                    change24hour=data['RAW'][_coin]['USD'].get('CHANGE24HOUR', 0),
                    changepct24hour=data['RAW'][_coin]['USD'].get('CHANGEPCT24HOUR', 0),
                    changeday=data['RAW'][_coin]['USD'].get('CHANGEDAY', 0),
                    changepctday=data['RAW'][_coin]['USD'].get('CHANGEPCTDAY', 0),
                    supply=data['RAW'][_coin]['USD'].get('SUPPLY', 0),
                    mktcap=data['RAW'][_coin]['USD'].get('MKTCAP', 0),
                    totalvolume24h=data['RAW'][_coin]['USD'].get('TOTALVOLUME24H', 0),
                    totalvolume24hto=data['RAW'][_coin]['USD'].get('TOTALVOLUME24HTO', 0),
                    fromsymbol=data['DISPLAY'][_coin]['USD'].get('FROMSYMBOL', 0)
                )
            except Exception, e:
                print str(e)
                print _coin

def get_detail():
    for coin in Coin.objects.all():
        try:
            url = 'https://www.cryptocompare.com/api/data/coinsnapshotfullbyid/?id={}'.format(coin.id)
            result = requests.get(url).json()['Data']
            coin.baseurl = result['SEO']['BaseUrl']
            coin.baseimageurl = result['SEO']['BaseImageUrl']
            if result['General'].get('StartDate'):
                coin.startdate = datetime.strptime(result['General'].get('StartDate'), '%d/%m/%Y')
            coin.twitter = result['General'].get('Twitter')
            coin.affiliateurl = result['General'].get('AffiliateUrl')
            coin.save()
        except Exception, e:
            print str(e)
            print coin.symbol


if __name__ == '__main__':
    if sys.argv[1] == 'hetch1':
        get_coins()
        get_prices()
    else:
        get_detail()
